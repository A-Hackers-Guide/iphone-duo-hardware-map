# `AppleKeyboardStateManager`

- Image: [`/System/Library/HIDPlugins/IOHIDKeyboardFilter.plugin/IOHIDKeyboardFilter`](../userland/System__Library__HIDPlugins__IOHIDKeyboardFilter.plugin__IOHIDKeyboardFilter.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _capsLockStateTable;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_capsLockStateTable) capsLockStateTable;
```

## Class methods

```
+[AppleKeyboardStateManager sharedManager];
```

## Instance methods

```
-[AppleKeyboardStateManager init];
-[AppleKeyboardStateManager capsLockStateTable];
-[AppleKeyboardStateManager isCapsLockEnabled:];
-[AppleKeyboardStateManager setCapsLockEnabled:locationID:];
-[AppleKeyboardStateManager setCapsLockStateTable:];
```
