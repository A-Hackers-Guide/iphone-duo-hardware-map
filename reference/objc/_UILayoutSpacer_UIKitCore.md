# `_UILayoutSpacer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UILayoutGuide`
- Protocols: `UILayoutSupport`
- 3 instance variables, 12 properties, 14 instance methods, 2 class methods

## Instance variables

```
B _compatibilityGuideAllowsArchivingAsSubview;
B _horizontal;
@"NSArray" _constraintsToRemoveAtRuntime;
```

## Properties

```
@property (TB,N,G_isHorizontal,S_setHorizontal:,V_horizontal) _horizontal;
@property (TB,N,S_setCompatibilityGuideAllowsArchivingAsSubview:,V_compatibilityGuideAllowsArchivingAsSubview) _compatibilityGuideAllowsArchivingAsSubview;
@property (T@"NSArray",C,N,S_setConstraintsToRemoveAtRuntime:,V_constraintsToRemoveAtRuntime) _constraintsToRemoveAtRuntime;
@property (T@"NSString",C,N,S_setArchivedIdentifier:) _archivedIdentifier;
@property (Td,R,N) length;
@property (T@"NSLayoutYAxisAnchor",R) topAnchor;
@property (T@"NSLayoutYAxisAnchor",R) bottomAnchor;
@property (T@"NSLayoutDimension",R) heightAnchor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UILayoutSpacer _horizontalLayoutSpacer];
+[_UILayoutSpacer _verticalLayoutSpacer];
```

## Instance methods

```
-[_UILayoutSpacer _setArchivedIdentifier:];
-[_UILayoutSpacer dealloc];
-[_UILayoutSpacer _archivedIdentifier];
-[_UILayoutSpacer _compatibilityGuideAllowsArchivingAsSubview];
-[_UILayoutSpacer length];
-[_UILayoutSpacer _constraintsToRemoveAtRuntime];
-[_UILayoutSpacer _setConstraintsToRemoveAtRuntime:];
-[_UILayoutSpacer encodeWithCoder:];
-[_UILayoutSpacer _setUpCounterDimensionConstraint];
-[_UILayoutSpacer _layoutVariablesWithAmbiguousValue];
-[_UILayoutSpacer initWithCoder:];
-[_UILayoutSpacer _isHorizontal];
-[_UILayoutSpacer _setHorizontal:];
-[_UILayoutSpacer _setCompatibilityGuideAllowsArchivingAsSubview:];
```
