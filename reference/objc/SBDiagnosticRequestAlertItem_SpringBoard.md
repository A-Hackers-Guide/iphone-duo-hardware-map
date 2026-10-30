# `SBDiagnosticRequestAlertItem`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAlertItem`
- 12 instance variables, 12 properties, 34 instance methods, 0 class methods

## Instance variables

```
@? _completionBlock;
@"NSString" _title;
@"NSString" _message;
@"NSString" _radarTitle;
@"NSString" _radarDescription;
@"NSNumber" _radarComponentID;
@"NSString" _radarComponentName;
@"NSString" _radarComponentVersion;
@"NSArray" _radarKeywordIDs;
@"NSArray" _radarAttachments;
q _radarClassification;
q _radarReproducibility;
```

## Properties

```
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",C,N,V_message) message;
@property (T@"NSString",C,N,V_radarTitle) radarTitle;
@property (T@"NSString",C,N,V_radarDescription) radarDescription;
@property (T@"NSNumber",C,N,V_radarComponentID) radarComponentID;
@property (T@"NSString",C,N,V_radarComponentName) radarComponentName;
@property (T@"NSString",C,N,V_radarComponentVersion) radarComponentVersion;
@property (T@"NSArray",C,N,V_radarKeywordIDs) radarKeywordIDs;
@property (T@"NSArray",C,N,V_radarAttachments) radarAttachments;
@property (Tq,N,V_radarClassification) radarClassification;
@property (Tq,N,V_radarReproducibility) radarReproducibility;
```

## Instance methods

```
-[SBDiagnosticRequestAlertItem setCompletionBlock:];
-[SBDiagnosticRequestAlertItem completionBlock];
-[SBDiagnosticRequestAlertItem setMessage:];
-[SBDiagnosticRequestAlertItem reappearsAfterUnlock];
-[SBDiagnosticRequestAlertItem reappearsAfterLock];
-[SBDiagnosticRequestAlertItem message];
-[SBDiagnosticRequestAlertItem performUnlockAction];
-[SBDiagnosticRequestAlertItem configure:requirePasscodeForActions:];
-[SBDiagnosticRequestAlertItem title];
-[SBDiagnosticRequestAlertItem shouldShowInLockScreen];
-[SBDiagnosticRequestAlertItem setTitle:];
-[SBDiagnosticRequestAlertItem radarDescription];
-[SBDiagnosticRequestAlertItem setRadarDescription:];
-[SBDiagnosticRequestAlertItem _fileRadar];
-[SBDiagnosticRequestAlertItem radarComponentID];
-[SBDiagnosticRequestAlertItem radarComponentName];
-[SBDiagnosticRequestAlertItem radarComponentVersion];
-[SBDiagnosticRequestAlertItem radarTitle];
-[SBDiagnosticRequestAlertItem setRadarTitle:];
-[SBDiagnosticRequestAlertItem radarClassification];
-[SBDiagnosticRequestAlertItem radarKeywordIDs];
-[SBDiagnosticRequestAlertItem _yesButtonTitle];
-[SBDiagnosticRequestAlertItem _noButtonTitle];
-[SBDiagnosticRequestAlertItem _stringFromClassification:];
-[SBDiagnosticRequestAlertItem _stringFromReproducibility:];
-[SBDiagnosticRequestAlertItem radarAttachments];
-[SBDiagnosticRequestAlertItem radarReproducibility];
-[SBDiagnosticRequestAlertItem setRadarAttachments:];
-[SBDiagnosticRequestAlertItem setRadarClassification:];
-[SBDiagnosticRequestAlertItem setRadarComponentID:];
-[SBDiagnosticRequestAlertItem setRadarComponentName:];
-[SBDiagnosticRequestAlertItem setRadarComponentVersion:];
-[SBDiagnosticRequestAlertItem setRadarKeywordIDs:];
-[SBDiagnosticRequestAlertItem setRadarReproducibility:];
```
