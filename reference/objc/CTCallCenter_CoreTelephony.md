# `CTCallCenter`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CXCallObserverDelegate`
- 5 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
{queue="fObj"{object="fObj"^{dispatch_object_s}}} _queue;
{queue="fObj"{object="fObj"^{dispatch_object_s}}} clientQueue;
@"NSSet" _currentCalls;
@? _callEventHandler;
@"CXCallObserver" _callKitObserver;
```

## Properties

```
@property (T@"CXCallObserver",&,V_callKitObserver) callKitObserver;
@property (T@"NSSet",&,D) currentCalls;
@property (T@?,C,N) callEventHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CTCallCenter initWithQueue:];
-[CTCallCenter init];
-[CTCallCenter dealloc];
-[CTCallCenter callObserver:callChanged:];
-[CTCallCenter currentCalls];
-[CTCallCenter description];
-[CTCallCenter setCurrentCalls:];
-[CTCallCenter callKitObserver];
-[CTCallCenter calculateCallStateChanges_sync:];
-[CTCallCenter callEventHandler];
-[CTCallCenter getCurrentCallSetFromServer_sync:];
-[CTCallCenter handleCallStatusChange_sync:];
-[CTCallCenter setCallEventHandler:];
-[CTCallCenter setCallKitObserver:];
```
