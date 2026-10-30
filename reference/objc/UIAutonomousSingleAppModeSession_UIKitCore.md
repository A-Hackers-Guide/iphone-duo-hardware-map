# `UIAutonomousSingleAppModeSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 9 instance methods, 4 class methods

## Instance variables

```
B _active;
@"UIAutonomousSingleAppModeConfiguration" _effectiveConfiguration;
```

## Properties

```
@property (T@"UIAutonomousSingleAppModeConfiguration",C,N,V_effectiveConfiguration) effectiveConfiguration;
@property (TB,N,GisActive,V_active) active;
```

## Class methods

```
+[UIAutonomousSingleAppModeSession __gaxTrampoline_currentlyActiveSession];
+[UIAutonomousSingleAppModeSession __gaxTrampoline_requestSessionWithConfiguration:completion:];
+[UIAutonomousSingleAppModeSession currentlyActiveSession];
+[UIAutonomousSingleAppModeSession requestSessionWithConfiguration:completion:];
```

## Instance methods

```
-[UIAutonomousSingleAppModeSession dealloc];
-[UIAutonomousSingleAppModeSession setActive:];
-[UIAutonomousSingleAppModeSession isActive];
-[UIAutonomousSingleAppModeSession initWithEffectiveConfiguration:];
-[UIAutonomousSingleAppModeSession __gaxTrampoline_endSessionWithCompletion:];
-[UIAutonomousSingleAppModeSession _guidedAccessStateDidChange:];
-[UIAutonomousSingleAppModeSession effectiveConfiguration];
-[UIAutonomousSingleAppModeSession endWithCompletion:];
-[UIAutonomousSingleAppModeSession setEffectiveConfiguration:];
```
