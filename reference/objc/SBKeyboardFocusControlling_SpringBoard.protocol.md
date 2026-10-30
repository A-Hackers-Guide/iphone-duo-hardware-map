# `SBKeyboardFocusControlling` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SBWindowSceneAttachmentObserving`
- 0 instance variables, 10 properties, 26 instance methods, 0 class methods

## Properties

```
@property (T@"NSSet",C) externalSceneIdentities;
@property (TQ,R,N) userFocusRequestGeneration;
@property (T@"FBScene",R,N) externalSceneWithFocus;
@property (TB,R) hasExternalSceneWithFocus;
@property (T@"<SBProductivityGestureDestinationProviding>",R,N) sceneWithFocusIncludingSpringBoard;
@property (T@"SBWindowScene",R,N) windowSceneWithFocus;
@property (T@"NSString",R,N) windowSceneIdentifierHostingFocusedAppScene;
@property (T@"UIWindow",R,N) windowWithFocus;
@property (T@"SBInputUISceneController",R,N) inputUISceneController;
@property (Ti,R,N) presentingKeyboardProcessIdentifier;
```

## Instance methods

```
-[SBKeyboardFocusControlling userFocusRequestForScene:requestReason:completion:];
-[SBKeyboardFocusControlling bufferEventsForSpringBoardScene:reason:];
-[SBKeyboardFocusControlling preventFocusForSceneWithIdentityToken:reason:];
-[SBKeyboardFocusControlling userFocusRequestForScene:reason:completion:];
-[SBKeyboardFocusControlling addKeyboardFocusObserver:];
-[SBKeyboardFocusControlling userFocusRequestForWindow:requestReason:completion:];
-[SBKeyboardFocusControlling establishConstraint:onTarget:reason:];
-[SBKeyboardFocusControlling externalSceneWithFocus];
-[SBKeyboardFocusControlling externalSceneIdentities];
-[SBKeyboardFocusControlling hasExternalSceneWithFocus];
-[SBKeyboardFocusControlling redirectFocusForReason:fromProcessIdentifier:fromSceneIdentityToken:toProcessIdentifier:toSceneIdentityToken:inContainingWindow:];
-[SBKeyboardFocusControlling windowWithFocus];
-[SBKeyboardFocusControlling inputUISceneController];
-[SBKeyboardFocusControlling requestArbitrationForSBWindowScene:forReason:];
-[SBKeyboardFocusControlling presentingKeyboardProcessIdentifier];
-[SBKeyboardFocusControlling removeKeyboardFocusFromScene:];
-[SBKeyboardFocusControlling windowSceneWithFocus];
-[SBKeyboardFocusControlling userFocusRequestGeneration];
-[SBKeyboardFocusControlling deferAdditionalEnvironments:whenTargetHasKeyboardFocus:];
-[SBKeyboardFocusControlling shouldAllowInteractionTrackingKeyboardFocusUpdateForWindow:];
-[SBKeyboardFocusControlling sceneWithFocusIncludingSpringBoard];
-[SBKeyboardFocusControlling suppressKeyboardFocusEvaluationForReason:];
-[SBKeyboardFocusControlling deferFromSBWindowScene:toTarget:lockReason:];
-[SBKeyboardFocusControlling noteSceneKeyboardShouldBeJailed:];
-[SBKeyboardFocusControlling windowSceneIdentifierHostingFocusedAppScene];
-[SBKeyboardFocusControlling setExternalSceneIdentities:];
```
