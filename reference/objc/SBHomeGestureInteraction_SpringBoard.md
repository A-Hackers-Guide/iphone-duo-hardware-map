# `SBHomeGestureInteraction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `SBSystemGestureRecognizerDelegate`, `SBTouchTemplateGestureRecognizerDelegate`
- 7 instance variables, 14 properties, 37 instance methods, 0 class methods

## Instance variables

```
B _enabled;
q _recognizedGestureType;
@"SBHomeGesturePanGestureRecognizer" _screenEdgePanGestureRecognizer;
@"SBIndirectPanGestureRecognizer" _indirectPanGestureRecognizer;
@"SBFluidScrunchGestureRecognizer" _scrunchGestureRecognizer;
@"<SBHomeGestureInteractionDelegate>" _delegate;
@"SBSystemGestureManager" _gestureManager;
```

## Properties

```
@property (T@"SBHomeGesturePanGestureRecognizer",&,N,V_screenEdgePanGestureRecognizer) screenEdgePanGestureRecognizer;
@property (T@"SBIndirectPanGestureRecognizer",&,N,V_indirectPanGestureRecognizer) indirectPanGestureRecognizer;
@property (T@"SBFluidScrunchGestureRecognizer",&,N,V_scrunchGestureRecognizer) scrunchGestureRecognizer;
@property (T@"<SBHomeGestureInteractionDelegate>",W,N,V_delegate) delegate;
@property (Tq,N,V_recognizedGestureType) recognizedGestureType;
@property (T@"SBSystemGestureManager",&,N,V_gestureManager) gestureManager;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (T@"NSSet",R,N) gestureRecognizers;
@property (T@"UIGestureRecognizer",R,N) recognizedGestureRecognizer;
@property (Td,R,N) indirectScreenEdgeGestureRecognitionDistance;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBHomeGestureInteraction translationInView:];
-[SBHomeGestureInteraction velocityInView:];
-[SBHomeGestureInteraction _configureScrunchGestureRecognizer];
-[SBHomeGestureInteraction gestureRecognizers];
-[SBHomeGestureInteraction gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[SBHomeGestureInteraction _configureGestureRecognizers];
-[SBHomeGestureInteraction indirectPanGestureRecognizer];
-[SBHomeGestureInteraction _handleGestureRecognizer:];
-[SBHomeGestureInteraction gestureRecognizer:shouldReceiveTouch:];
-[SBHomeGestureInteraction recognizedGestureType];
-[SBHomeGestureInteraction setIndirectPanGestureRecognizer:];
-[SBHomeGestureInteraction gestureRecognizerForType:];
-[SBHomeGestureInteraction setScrunchGestureRecognizer:];
-[SBHomeGestureInteraction dealloc];
-[SBHomeGestureInteraction typeOfGestureRecognizer:];
-[SBHomeGestureInteraction _isGestureRunning:];
-[SBHomeGestureInteraction _configureIndirectPanGestureRecognizer];
-[SBHomeGestureInteraction screenEdgePanGestureRecognizer];
-[SBHomeGestureInteraction gestureManager];
-[SBHomeGestureInteraction viewForSystemGestureRecognizer:];
-[SBHomeGestureInteraction locationInView:];
-[SBHomeGestureInteraction isEnabled];
-[SBHomeGestureInteraction invalidate];
-[SBHomeGestureInteraction setGestureManager:];
-[SBHomeGestureInteraction setDelegate:];
-[SBHomeGestureInteraction initWithSystemGestureManager:delegate:];
-[SBHomeGestureInteraction recognizedGestureRecognizer];
-[SBHomeGestureInteraction gestureRecognizerShouldBegin:];
-[SBHomeGestureInteraction _configureScreenEdgePanGestureRecognizer];
-[SBHomeGestureInteraction setEnabled:];
-[SBHomeGestureInteraction gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[SBHomeGestureInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBHomeGestureInteraction delegate];
-[SBHomeGestureInteraction setRecognizedGestureType:];
-[SBHomeGestureInteraction setScreenEdgePanGestureRecognizer:];
-[SBHomeGestureInteraction indirectScreenEdgeGestureRecognitionDistance];
-[SBHomeGestureInteraction scrunchGestureRecognizer];
```
