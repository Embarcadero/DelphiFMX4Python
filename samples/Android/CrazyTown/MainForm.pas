(**************************************************************************)
(*                                                                        *)
(* Module:  Unit 'MainForm'     Copyright (c) 2021                        *)
(*                                                                        *)
(*                                  Lucas Moura Belo - lmbelo             *)
(*                                  lucas.belo@live.com                   *)
(*                                  Brazil                                *)
(*                                                                        *)
(**************************************************************************)
(*  Functionality:  MainForm of PyFun                                     *)
(*                  PyFun on Android                                      *)
(*                                                                        *)
(**************************************************************************)
(* This source code is distributed with no WARRANTY, for no reason or use.*)
(* Everyone is allowed to use and change this code free for his own tasks *)
(* and projects, as long as this header and its copyright text is intact. *)
(* For changed versions of this code, which are public distributed the    *)
(* following additional conditions have to be fullfilled:                 *)
(* 1) The header has to contain a comment on the change and the author of *)
(*    it.                                                                 *)
(* 2) A copy of the changed source has to be sent to the above E-Mail     *)
(*    address or my then valid address, if this is possible to the        *)
(*    author.                                                             *)
(* The second condition has the target to maintain an up to date central  *)
(* version of the component. If this condition is not acceptable for      *)
(* confidential or legal reasons, everyone is free to derive a component  *)
(* or to generate a diff file to my or other original sources.            *)
(**************************************************************************)

unit MainForm;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.Memo.Types,
  FMX.Ani, FMX.StdCtrls, FMX.Controls.Presentation, FMX.ScrollBox, FMX.Memo,
  PythonEngine, FMX.PythonGUIInputOutput, System.Actions, FMX.ActnList,
  FMX.Objects, FMX.Layouts, FMX.Platform, AppEnvironment, ProgressFrame,
  System.Threading, FMX.ListBox, WrapDelphi, WrapDelphiFMX;

type
  TPyMainForm = class(TForm)
    tbTop: TToolBar;
    PythonEngine1: TPythonEngine;
    ActionList1: TActionList;
    actRun: TAction;
    Label1: TLabel;
    StyleBook1: TStyleBook;
    PyDelphiWrapper1: TPyDelphiWrapper;
    PythonModule1: TPythonModule;
    tbBottom: TToolBar;
    btnRun: TButton;
    mmMainScript: TMemo;
    mmOutput: TMemo;
    spInputOutput: TSplitter;
    RoundRect1: TRoundRect;
    PythonGUIInputOutput1: TPythonGUIInputOutput;
    procedure FormCreate(Sender: TObject);
    procedure FormDestroy(Sender: TObject);
    procedure actRunExecute(Sender: TObject);
  private
    FAppEnv: TAppEnvironment;
    function AppEventHandler(AAppEvent: TApplicationEvent; AContext: TObject): boolean;
    procedure ConfigurePython();
    procedure DisableComponents();
    procedure EnableComponents();
    function TryLoadingMainScript(): boolean;
    procedure RunMainScript();
  public
    { Public declarations }
  end;

var
  PyMainForm: TPyMainForm;

implementation

uses
  PythonLoad, System.IOUtils;

{$R *.fmx}

{ TPyMainForm }

procedure TPyMainForm.FormCreate(Sender: TObject);
begin
  DisableComponents();
  FAppEnv := TAppEnvironment.Create(TProgressViewFrame.Create(Self, Self));

  var LAppEventService := IFMXApplicationEventService(nil);
  if TPlatformServices.Current.SupportsPlatformService(
    IFMXApplicationEventService, IInterface(LAppEventService)) then
      LAppEventService.SetApplicationEventHandler(AppEventHandler)
  else begin
    Log.d('Platform service "IFMXApplicationEventService" not supported.');
    Halt(1);
  end;
end;

procedure TPyMainForm.FormDestroy(Sender: TObject);
begin
  FAppEnv.Free();
end;

procedure TPyMainForm.RunMainScript;
begin
  PythonEngine1.ExecString(AnsiString(mmMainScript.Lines.Text));
end;

function TPyMainForm.TryLoadingMainScript: boolean;
begin
  var LScript := TPath.Combine(TPath.GetDocumentsPath(), 'Form6.py');
  Result := TFile.Exists(LScript);
  if Result then begin
    mmMainScript.Lines.Text := TFile.ReadAllText(LScript)
      .Replace('%PATH%', TPath.GetDocumentsPath());
  end;
end;

procedure TPyMainForm.actRunExecute(Sender: TObject);
begin
  PythonEngine1.ExecString(AnsiString(mmMainScript.Lines.Text));
end;

function TPyMainForm.AppEventHandler(AAppEvent: TApplicationEvent;
  AContext: TObject): boolean;
begin
  case AAppEvent of
    TApplicationEvent.FinishedLaunching: ConfigurePython();
  end;
  Result := true;
end;

procedure TPyMainForm.ConfigurePython;
begin
  FAppEnv.InitializeEnvironmentAsync(PythonEngine1, true,
    procedure(const AInitialized: boolean; const ALastErrorMsg: string) begin
      TThread.Synchronize(nil,
        procedure begin
          if AInitialized then begin
            if TryLoadingMainScript() then
              RunMainScript()
            else
              ShowMessage('Unabled to run the script.');
            EnableComponents();
          end else
            ShowMessage(ALastErrorMsg);
        end);
    end);
end;

procedure TPyMainForm.DisableComponents;
begin
  btnRun.Enabled := false;
end;

procedure TPyMainForm.EnableComponents;
begin
  btnRun.Enabled := true;
end;

end.
