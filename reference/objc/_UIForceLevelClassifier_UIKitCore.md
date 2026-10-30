# `_UIForceLevelClassifier`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSObserver`
- 7 instance variables, 8 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSObservationSource" _progressTouchForceObservable;
@"NSMutableDictionary" _cachedProgressObservables;
@"NSArray" _delegateObservations;
B _respectsSystemGestureTouchFiltering;
q _currentForceLevel;
@"<_UIForceLevelClassifierDelegate>" _delegate;
d _currentTouchForceMultiplier;
```

## Properties

```
@property (Td,N,V_currentTouchForceMultiplier) currentTouchForceMultiplier;
@property (TB,N,V_respectsSystemGestureTouchFiltering) respectsSystemGestureTouchFiltering;
@property (T@"<_UIForceLevelClassifierDelegate>",W,N,V_delegate) delegate;
@property (Tq,R,N,V_currentForceLevel) currentForceLevel;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIForceLevelClassifier init];
-[_UIForceLevelClassifier dealloc];
-[_UIForceLevelClassifier reset];
-[_UIForceLevelClassifier setDelegate:];
-[_UIForceLevelClassifier receiveObservedValue:];
-[_UIForceLevelClassifier delegate];
-[_UIForceLevelClassifier setCurrentTouchForceMultiplier:];
-[_UIForceLevelClassifier _accessibilityForceSensitivityChanged:];
-[_UIForceLevelClassifier _notifyDelegateOfProgress:toForceLevel:];
-[_UIForceLevelClassifier currentForceLevel];
-[_UIForceLevelClassifier currentTouchForceMultiplier];
-[_UIForceLevelClassifier observableForProgressToForceLevel:];
-[_UIForceLevelClassifier observableForProgressToForceLevel:minimumRequiredForceLevel:];
-[_UIForceLevelClassifier observeTouchWithForceValue:atTimestamp:withCentroidAtLocation:];
-[_UIForceLevelClassifier respectsSystemGestureTouchFiltering];
-[_UIForceLevelClassifier setCurrentForceLevel:];
-[_UIForceLevelClassifier setRespectsSystemGestureTouchFiltering:];
-[_UIForceLevelClassifier touchForceMultiplierDidChange];
-[_UIForceLevelClassifier wantsUnclampedForceValues];
```
