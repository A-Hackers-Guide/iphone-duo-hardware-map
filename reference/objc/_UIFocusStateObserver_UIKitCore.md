# `_UIFocusStateObserver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _observers;
{?="wasActive"b1"supressNotifyObservers"b1} _flags;
```

## Properties

```
@property (TB,R,N,GisActive) active;
```

## Instance methods

```
-[_UIFocusStateObserver removeObserver:];
-[_UIFocusStateObserver init];
-[_UIFocusStateObserver addObserver:];
-[_UIFocusStateObserver description];
-[_UIFocusStateObserver isActive];
-[_UIFocusStateObserver descriptionBuilder];
-[_UIFocusStateObserver performUpdatesAndNotifyObservers:];
-[_UIFocusStateObserver notifyObserversIfNecessary];
```
