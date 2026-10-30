# `SBAppExposeToHomeWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 3 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _transitionID;
@"SBAppExposeWindowingModifier" _appExposeModifier;
@"NSArray" _adjustedAppLayoutsBeforeTransition;
```

## Instance methods

```
-[SBAppExposeToHomeWindowingModifier adjustedAppLayoutsForAppLayouts:];
-[SBAppExposeToHomeWindowingModifier transitionWillBegin:];
-[SBAppExposeToHomeWindowingModifier willBegin];
-[SBAppExposeToHomeWindowingModifier didComplete];
-[SBAppExposeToHomeWindowingModifier initWithTransitionModifier:appExposeModifier:];
-[SBAppExposeToHomeWindowingModifier shouldInterruptForActivity:];
-[SBAppExposeToHomeWindowingModifier transitionDidComplete:];
```
