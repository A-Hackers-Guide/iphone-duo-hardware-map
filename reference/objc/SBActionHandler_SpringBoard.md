# `SBActionHandler`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFActionProviding`
- 1 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSHashTable" _externalHandlers;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBActionHandler sharedInstance];
```

## Instance methods

```
-[SBActionHandler removeActionHandler:];
-[SBActionHandler addActionHandler:];
-[SBActionHandler _executeRestartAction:fromProcess:];
-[SBActionHandler _handleCloseApplicationAction:];
-[SBActionHandler _handleShowHomeScreenAction:];
-[SBActionHandler _reportAndKillInsecureProcesses:];
-[SBActionHandler handleActions:origin:withResult:];
-[SBActionHandler handleClientWorkspaceActions:];
```
