# `SBApplicationTestingManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _queue_testEndedHandlers;
@"NSMutableDictionary" _idleTimerDisableAssertions;
@"NSString" _currentTestName;
@"NSString" _scrollTestActiveSubtest;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,G_idleTimerDisableAssertions,V_idleTimerDisableAssertions) idleTimerDisableAssertions;
@property (T@"NSString",C,N,V_currentTestName) currentTestName;
@property (T@"NSString",C,N,V_scrollTestActiveSubtest) scrollTestActiveSubtest;
```

## Class methods

```
+[SBApplicationTestingManager sharedInstance];
```

## Instance methods

```
-[SBApplicationTestingManager init];
-[SBApplicationTestingManager _idleTimerDisableAssertions];
-[SBApplicationTestingManager installNotificationObserverForNotificationName:forOneNotification:usingBlock:];
-[SBApplicationTestingManager currentTestName];
-[SBApplicationTestingManager setCurrentTestName:];
-[SBApplicationTestingManager _handleTestEnded];
-[SBApplicationTestingManager _installTestEndedHandler:];
-[SBApplicationTestingManager _prepareForTestStartup:];
-[SBApplicationTestingManager installNotificationObserverForNotificationName:notificationCenter:forOneNotification:usingBlock:];
-[SBApplicationTestingManager markUserLaunchInitiationTime];
-[SBApplicationTestingManager scrollTestActiveSubtest];
-[SBApplicationTestingManager setScrollTestActiveSubtest:];
-[SBApplicationTestingManager setupKeyboardAnimationSubTestsForTestName:];
```
