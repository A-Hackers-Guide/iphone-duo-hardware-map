# `_UIKeyWindowEvaluator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDebugDescriptionProviding`
- 7 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
[11Q] _countOfFBSSceneBackedScenesByShiftedIdiom;
[11Q] _defaultEvaluationStrategyByShiftedIdiom;
@"_UIKeyWindowSceneStack" _keyWindowSceneStack;
@"_UIKeyWindowSceneStack" _excludedSceneStack;
@"_UIKeyWindowSceneStack" _stackForSceneMovingScreens;
@"UIWindow" _applicationKeyWindow;
@"<BSInvalidatable>" _stateCaptureToken;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIKeyWindowEvaluator sharedEvaluator];
```

## Instance methods

```
-[_UIKeyWindowEvaluator debugDescription];
-[_UIKeyWindowEvaluator succinctDescriptionBuilder];
-[_UIKeyWindowEvaluator dealloc];
-[_UIKeyWindowEvaluator descriptionWithMultilinePrefix:];
-[_UIKeyWindowEvaluator succinctDescription];
-[_UIKeyWindowEvaluator debugDescriptionWithMultilinePrefix:];
-[_UIKeyWindowEvaluator description];
-[_UIKeyWindowEvaluator descriptionBuilderWithMultilinePrefix:];
```
