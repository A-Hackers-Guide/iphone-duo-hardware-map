# `FBSDisplayLayoutPublisher`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `FBSDisplayLayoutPublishing`, `BSInvalidatable`
- 14 instance variables, 9 properties, 27 instance methods, 1 class methods

## Instance variables

```
@"BSAtomicSignal" _invalidatedSignal;
@"BSServiceConnectionListener" _listener;
[3@"BSServiceDispatchQueue"] _queuesByQOS;
[3@"NSObject<OS_xpc_object>"] _queues_xLayoutByQOS;
[3@"NSMutableSet"] _queues_connectionsByQOS;
@"FBSDisplayLayout" _mutableLayout;
@"NSMutableSet" _mutableElementKeys;
@"NSHashTable" _observers;
@"NSObject<OS_xpc_object>" _xLayout;
@"FBSDisplayLayout" _currentLayout;
@"NSMutableOrderedSet" _transitionReasons;
Q _transitionsCount;
Q _suppressionCount;
B _dirty;
```

## Properties

```
@property (T@"FBSDisplayConfiguration",C,N) displayConfiguration;
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
+[FBSDisplayLayoutPublisher publisherWithConfiguration:];
```

## Instance methods

```
-[FBSDisplayLayoutPublisher setBacklightState:];
-[FBSDisplayLayoutPublisher interfaceOrientation];
-[FBSDisplayLayoutPublisher listener:didReceiveConnection:withContext:];
-[FBSDisplayLayoutPublisher setBacklightLevel:];
-[FBSDisplayLayoutPublisher displayConfiguration];
-[FBSDisplayLayoutPublisher addElement:];
-[FBSDisplayLayoutPublisher backlightLevel];
-[FBSDisplayLayoutPublisher setInterfaceOrientation:];
-[FBSDisplayLayoutPublisher removeObserver:];
-[FBSDisplayLayoutPublisher init];
-[FBSDisplayLayoutPublisher flush];
-[FBSDisplayLayoutPublisher add:];
-[FBSDisplayLayoutPublisher isTransitioning];
-[FBSDisplayLayoutPublisher remove:];
-[FBSDisplayLayoutPublisher dealloc];
-[FBSDisplayLayoutPublisher _endTransition];
-[FBSDisplayLayoutPublisher _endSuppression];
-[FBSDisplayLayoutPublisher _addElement:forKey:];
-[FBSDisplayLayoutPublisher currentLayout];
-[FBSDisplayLayoutPublisher suppressLayoutForReason:];
-[FBSDisplayLayoutPublisher setDisplayConfiguration:];
-[FBSDisplayLayoutPublisher _removeElement:forKey:];
-[FBSDisplayLayoutPublisher addObserver:];
-[FBSDisplayLayoutPublisher invalidate];
-[FBSDisplayLayoutPublisher _initWithConfiguration:];
-[FBSDisplayLayoutPublisher activate];
-[FBSDisplayLayoutPublisher transitionAssertionWithReason:];
```
