# `SBKeyboardFocusArbitrationReason`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`
- 3 instance variables, 6 properties, 10 instance methods, 35 class methods

## Instance variables

```
@"NSString" _sourceName;
B _fromKeyboardArbiter;
@"NSString" _label;
```

## Properties

```
@property (TB,R,N) isKeyboardArbiterSuggestion;
@property (T@"NSString",R,C,N,V_label) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBKeyboardFocusArbitrationReason appFocusRedirections];
+[SBKeyboardFocusArbitrationReason accessibility:];
+[SBKeyboardFocusArbitrationReason didDismissTransientOverlayScene];
+[SBKeyboardFocusArbitrationReason didRemoveKeyboardFocusFromScene];
+[SBKeyboardFocusArbitrationReason transientOverlayDismissAllToAppsWorkspaceTransactionDidComplete];
+[SBKeyboardFocusArbitrationReason assistantControllerVisibility];
+[SBKeyboardFocusArbitrationReason backlightControllerDidAnimate];
+[SBKeyboardFocusArbitrationReason controlCenterDidAppear];
+[SBKeyboardFocusArbitrationReason deferAdditionalEnvironments];
+[SBKeyboardFocusArbitrationReason didChangeShowingSystemModalAlert];
+[SBKeyboardFocusArbitrationReason didResetCoalition];
+[SBKeyboardFocusArbitrationReason displayDidBecomeActive];
+[SBKeyboardFocusArbitrationReason dsahBoardAppViewControllerDidAppear];
+[SBKeyboardFocusArbitrationReason dsahBoardAppViewControllerDidDisappear];
+[SBKeyboardFocusArbitrationReason focusLockAssertionsDidChange];
+[SBKeyboardFocusArbitrationReason focusRedirectAssertionsDidChange];
+[SBKeyboardFocusArbitrationReason keyWindowNotification];
+[SBKeyboardFocusArbitrationReason keyboardArbiterSuggestion];
+[SBKeyboardFocusArbitrationReason keyboardFocusEvaluationSuppression];
+[SBKeyboardFocusArbitrationReason longLookDidDismissForNotificationViewController];
+[SBKeyboardFocusArbitrationReason longLookDidPresentForNotificationViewController];
+[SBKeyboardFocusArbitrationReason modalUIFluidDismissGestureDidFinish];
+[SBKeyboardFocusArbitrationReason preventFocusForPID];
+[SBKeyboardFocusArbitrationReason quickCameraDidAppear];
+[SBKeyboardFocusArbitrationReason removedCoalitionMember];
+[SBKeyboardFocusArbitrationReason removedKeyboardArbiterSceneDidRemove];
+[SBKeyboardFocusArbitrationReason removedKeyboardArbiterSceneWillRemove];
+[SBKeyboardFocusArbitrationReason showWindowedAccessoryWindow];
+[SBKeyboardFocusArbitrationReason spotlightMultiplexingDidBecomeActiveDelegate];
+[SBKeyboardFocusArbitrationReason spotlightMultiplexingDidCreateScene];
+[SBKeyboardFocusArbitrationReason spotlightMultiplexingDidDestroyScene];
+[SBKeyboardFocusArbitrationReason spotlightMultiplexingViewDidDisappear];
+[SBKeyboardFocusArbitrationReason transientOverlayDismissWorkspaceTransactionDidBegin];
+[SBKeyboardFocusArbitrationReason willPresentTransientOverlayScene];
+[SBKeyboardFocusArbitrationReason workspaceDidFinishInitialization];
```

## Instance methods

```
-[SBKeyboardFocusArbitrationReason label];
-[SBKeyboardFocusArbitrationReason _initWithLabel:];
-[SBKeyboardFocusArbitrationReason hash];
-[SBKeyboardFocusArbitrationReason description];
-[SBKeyboardFocusArbitrationReason appendDescriptionToStream:];
-[SBKeyboardFocusArbitrationReason isEqual:];
-[SBKeyboardFocusArbitrationReason _initForKeyboardArbiterWithLabel:];
-[SBKeyboardFocusArbitrationReason _initWithName:source:];
-[SBKeyboardFocusArbitrationReason annotatedWithSourceName:];
-[SBKeyboardFocusArbitrationReason isKeyboardArbiterSuggestion];
```
