# `SBGuidedAccessListener`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
B _isGuidedAccessActive;
```

## Properties

```
@property (TB,N,V_isGuidedAccessActive) isGuidedAccessActive;
```

## Class methods

```
+[SBGuidedAccessListener sharedGuidedAccessListener];
```

## Instance methods

```
-[SBGuidedAccessListener init];
-[SBGuidedAccessListener isGuidedAccessActive];
-[SBGuidedAccessListener guidedAccessWasActivated];
-[SBGuidedAccessListener guidedAccessWasDeactivated];
-[SBGuidedAccessListener setIsGuidedAccessActive:];
```
