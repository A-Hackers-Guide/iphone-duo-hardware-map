# `_UISceneEventDeferringHost` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 10 instance methods, 0 class methods

## Properties

```
@property (Tq,N) deferringRuleBehavior;
@property (Tq,N) selectionRequestBehavior;
@property (Tq,N) constraintAssertionBehavior;
@property (Tq,N) grantBehavior;
```

## Instance methods

```
-[_UISceneEventDeferringHost grantBehavior];
-[_UISceneEventDeferringHost constraintAssertionBehavior];
-[_UISceneEventDeferringHost imposeConstraintForReason:];
-[_UISceneEventDeferringHost selectionRequestBehavior];
-[_UISceneEventDeferringHost setConstraintAssertionBehavior:];
-[_UISceneEventDeferringHost setDeferringRuleBehavior:];
-[_UISceneEventDeferringHost setSelectionRequestBehavior:];
-[_UISceneEventDeferringHost performSelectionRequestIgnoringModalities:];
-[_UISceneEventDeferringHost deferringRuleBehavior];
-[_UISceneEventDeferringHost setGrantBehavior:];
```
