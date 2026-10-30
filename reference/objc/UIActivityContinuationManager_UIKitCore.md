# `UIActivityContinuationManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSUserActivityDelegate`
- 4 instance variables, 7 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"<UIActivityContinuationManagerApplicationContext>" _context;
@"NSString" _currentActivityContinuationType;
@"NSString" _currentActivityContinuationUUIDString;
@"NSProgress" _currentActivityContinuationProgress;
```

## Properties

```
@property (T@"NSString",C,N,G_currentActivityContinuationType,S_setCurrentActivityContinuationType:,V_currentActivityContinuationType) currentActivityContinuationType;
@property (T@"NSString",C,N,G_currentActivityContinuationUUIDString,S_setCurrentActivityContinuationUUIDString:,V_currentActivityContinuationUUIDString) currentActivityContinuationUUIDString;
@property (T@"NSProgress",&,N,G_currentActivityContinuationProgress,S_setCurrentActivityContinuationProgress:,V_currentActivityContinuationProgress) currentActivityContinuationProgress;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIActivityContinuationManager isTrackingActivityContinuationForResponder:document:userActivity:];
-[UIActivityContinuationManager activityContinuationsAreBeingTracked];
-[UIActivityContinuationManager activityContinuationDictionaryWithAction:sourceApplication:originatingProcess:];
-[UIActivityContinuationManager init];
-[UIActivityContinuationManager _userActivityWillSave:];
-[UIActivityContinuationManager _endCurrentActivityContinuationWithCompletion:];
-[UIActivityContinuationManager _displayCurrentActivityContinuationProgressUI];
-[UIActivityContinuationManager handleActivityContinuation:isSuspended:];
-[UIActivityContinuationManager _currentActivityContinuationUUIDString];
-[UIActivityContinuationManager _delegateHandledContinueActivityWithType:];
-[UIActivityContinuationManager _setCurrentActivityContinuationType:];
-[UIActivityContinuationManager removeResponder:document:forUserActivity:];
-[UIActivityContinuationManager _setCurrentActivityContinuationUUIDString:];
-[UIActivityContinuationManager _continueUserActivity:];
-[UIActivityContinuationManager userActivityWillSave:];
-[UIActivityContinuationManager _hideCurrentActivityContinuationProgressUI];
-[UIActivityContinuationManager _currentActivityContinuationProgress];
-[UIActivityContinuationManager addResponder:document:forUserActivity:];
-[UIActivityContinuationManager _setCurrentActivityContinuationProgress:];
-[UIActivityContinuationManager initWithApplicationContext:];
-[UIActivityContinuationManager _currentActivityContinuationType];
-[UIActivityContinuationManager _didFailToContinueUserActivityWithType:error:];
-[UIActivityContinuationManager _clearCurrentActivityContinuationCancelingProgress:];
-[UIActivityContinuationManager _endCurrentActivityContinuationAndDisplayError:];
-[UIActivityContinuationManager _fetchUserActivityWithUUID:completionHandler:];
-[UIActivityContinuationManager _cleanupUserActivity:activityIdentifier:];
```
