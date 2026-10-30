# `AVResourceReclamationController`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 1 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _stateQueue;
@"NSObject<OS_dispatch_queue>" _figSetterQueue;
@"NSObject<OS_dispatch_queue>" _callbackQueue;
@"NSMapTable" _resourceReclamationObservers;
@"NSMutableDictionary" _assertionReasons;
Q _assertionId;
B _isEnrolled;
@ _notificationToken;
```

## Properties

```
@property (T@"AVResourceReclamationEvent",R) mostRecentReclamationEvent;
```

## Class methods

```
+[AVResourceReclamationController defaultController];
```

## Instance methods

```
-[AVResourceReclamationController init];
-[AVResourceReclamationController dealloc];
-[AVResourceReclamationController permitReclamationWhileSuspended];
-[AVResourceReclamationController _releaseResourceReclamationAssertion:];
-[AVResourceReclamationController _removeObserverToken:];
-[AVResourceReclamationController _resetEnrollmentTestOnly];
-[AVResourceReclamationController addReclamationEventObserver:];
-[AVResourceReclamationController ensureIntegrityOfResourcesCreatedSince:];
-[AVResourceReclamationController ensureIntegrityOfResourcesCreatedSince:completionHandler:];
-[AVResourceReclamationController handlePurgedNotification:];
-[AVResourceReclamationController informReclamationEvent:toObservers:];
-[AVResourceReclamationController isEnrolled];
-[AVResourceReclamationController mostRecentReclamationEvent];
-[AVResourceReclamationController registerForPurgeNotification];
-[AVResourceReclamationController takeAssertionPreventingResourceReclamationWithReason:];
```
