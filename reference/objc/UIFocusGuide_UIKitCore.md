# `UIFocusGuide`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UILayoutGuide`
- Protocols: `_UIFocusGuideImplDelegate`
- 2 instance variables, 8 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"_UIFocusGuideImpl" _impl;
@"NSArray" _preferredFocusEnvironments;
```

## Properties

```
@property (T@"_UIFocusGuideImpl",R,N,V_impl) _impl;
@property (TB,N,GisEnabled) enabled;
@property (T@"NSArray",C,N,V_preferredFocusEnvironments) preferredFocusEnvironments;
@property (T@"UIView",W,N) preferredFocusedView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIFocusGuide _implClass];
```

## Instance methods

```
-[UIFocusGuide _encodablePreferredFocusEnvironments];
-[UIFocusGuide _setOwningView:];
-[UIFocusGuide init];
-[UIFocusGuide frameForFocusGuide:];
-[UIFocusGuide setPreferredFocusEnvironments:];
-[UIFocusGuide _didUpdateFocusToPreferredFocusedView];
-[UIFocusGuide isEnabled];
-[UIFocusGuide didUpdateFocusFromGuide:];
-[UIFocusGuide _uili_isFocusGuide];
-[UIFocusGuide setEnabled:];
-[UIFocusGuide encodeWithCoder:];
-[UIFocusGuide description];
-[UIFocusGuide preferredFocusEnvironments];
-[UIFocusGuide initWithCoder:];
-[UIFocusGuide _impl];
-[UIFocusGuide preferredFocusedView];
-[UIFocusGuide setPreferredFocusedView:];
```
