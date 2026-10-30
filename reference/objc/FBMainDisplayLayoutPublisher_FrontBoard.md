# `FBMainDisplayLayoutPublisher`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSDisplayObserving`, `FBSDisplayLayoutPublisherObserving`, `BLSBacklightStateObserving`, `BLSHBacklightHostObserving`, `FBSDisplayLayoutPublishing`
- 2 instance variables, 8 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"FBSDisplayLayoutPublisher" _publisher;
@"<BSInvalidatable>" _backlightTransition;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,N) interfaceOrientation;
@property (Tq,N) backlightLevel;
@property (TB,R,N,GisTransitioning) transitioning;
@property (T@"FBSDisplayLayout",R,N) currentLayout;
```

## Class methods

```
+[FBMainDisplayLayoutPublisher sharedInstance];
```

## Instance methods

```
-[FBMainDisplayLayoutPublisher backlight:didCompleteUpdateToState:forEvents:abortedEvents:];
-[FBMainDisplayLayoutPublisher interfaceOrientation];
-[FBMainDisplayLayoutPublisher setBacklightLevel:];
-[FBMainDisplayLayoutPublisher addElement:];
-[FBMainDisplayLayoutPublisher backlightLevel];
-[FBMainDisplayLayoutPublisher setInterfaceOrientation:];
-[FBMainDisplayLayoutPublisher removeObserver:];
-[FBMainDisplayLayoutPublisher init];
-[FBMainDisplayLayoutPublisher flush];
-[FBMainDisplayLayoutPublisher isTransitioning];
-[FBMainDisplayLayoutPublisher dealloc];
-[FBMainDisplayLayoutPublisher publisher:didUpdateLayout:withTransition:];
-[FBMainDisplayLayoutPublisher _addElement:forKey:];
-[FBMainDisplayLayoutPublisher currentLayout];
-[FBMainDisplayLayoutPublisher displayMonitor:didUpdateIdentity:withConfiguration:];
-[FBMainDisplayLayoutPublisher addObserver:];
-[FBMainDisplayLayoutPublisher backlightHost:willTransitionToState:forEvent:];
-[FBMainDisplayLayoutPublisher transitionAssertionWithReason:];
-[FBMainDisplayLayoutPublisher _initWithPublisher:];
-[FBMainDisplayLayoutPublisher _updateWithBacklightState:];
```
