# `UIFocusEnvironment` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T@"NSArray",R,C,N) preferredFocusEnvironments;
@property (T@"<UIFocusEnvironment>",R,W,N) parentFocusEnvironment;
@property (T@"<UIFocusItemContainer>",R,N) focusItemContainer;
@property (T@"UIView",?,R,W,N) preferredFocusedView;
@property (T@"NSString",?,R,C,N) focusGroupIdentifier;
```

## Instance methods

```
-[UIFocusEnvironment updateFocusIfNeeded];
-[UIFocusEnvironment didUpdateFocusInContext:withAnimationCoordinator:];
-[UIFocusEnvironment setNeedsFocusUpdate];
-[UIFocusEnvironment parentFocusEnvironment];
-[UIFocusEnvironment focusItemContainer];
-[UIFocusEnvironment preferredFocusEnvironments];
-[UIFocusEnvironment shouldUpdateFocusInContext:];
-[UIFocusEnvironment focusGroupIdentifier];
-[UIFocusEnvironment preferredFocusedView];
-[UIFocusEnvironment soundIdentifierForFocusUpdateInContext:];
```
