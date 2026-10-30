# `_UIAssertionBase`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIAssertion`
- 6 instance variables, 10 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _initialState;
B _invalidated;
B _requiresExplicitInvalidation;
Q _type;
@"NSString" _reason;
@"_UIAssertionController" _parentController;
```

## Properties

```
@property (TB,R,N,V_initialState) initialState;
@property (TQ,R,N,V_type) type;
@property (T@"NSString",R,N,V_reason) reason;
@property (T@"_UIAssertionController",W,N,V_parentController) parentController;
@property (TB,R,N,V_invalidated) invalidated;
@property (TB,R,N,V_requiresExplicitInvalidation) requiresExplicitInvalidation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIAssertionBase invalidated];
-[_UIAssertionBase _invalidate];
-[_UIAssertionBase dealloc];
-[_UIAssertionBase _initWithType:initialState:reason:requiresExplicitInvalidation:];
-[_UIAssertionBase type];
-[_UIAssertionBase description];
-[_UIAssertionBase requiresExplicitInvalidation];
-[_UIAssertionBase initialState];
-[_UIAssertionBase reason];
-[_UIAssertionBase parentController];
-[_UIAssertionBase setParentController:];
```
