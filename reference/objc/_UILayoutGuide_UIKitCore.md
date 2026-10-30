# `_UILayoutGuide`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UILayoutSupport`
- 4 instance variables, 12 properties, 16 instance methods, 3 class methods

## Instance variables

```
B _allowsArchivingAsSubview;
B _horizontal;
@"NSArray" _constraintsToRemoveAtRuntime;
@"NSString" _archivedIdentifier;
```

## Properties

```
@property (TB,N,GisHorizontal,S_setHorizontal:,V_horizontal) _horizontal;
@property (T@"NSString",C,N,S_setArchivedIdentifier:,V_archivedIdentifier) _archivedIdentifier;
@property (TB,N,S_setAllowsArchivingAsSubview:,V_allowsArchivingAsSubview) _allowsArchivingAsSubview;
@property (T@"NSArray",C,N,S_setConstraintsToRemoveAtRuntime:,V_constraintsToRemoveAtRuntime) _constraintsToRemoveAtRuntime;
@property (Td,R,N) length;
@property (T@"NSLayoutYAxisAnchor",R,D) topAnchor;
@property (T@"NSLayoutYAxisAnchor",R,D) bottomAnchor;
@property (T@"NSLayoutDimension",R,D) heightAnchor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UILayoutGuide classFallbacksForKeyedArchiver];
+[_UILayoutGuide _horizontalLayoutGuide];
+[_UILayoutGuide _verticalLayoutGuide];
```

## Instance methods

```
-[_UILayoutGuide _setArchivedIdentifier:];
-[_UILayoutGuide dealloc];
-[_UILayoutGuide _archivedIdentifier];
-[_UILayoutGuide length];
-[_UILayoutGuide _constraintsToRemoveAtRuntime];
-[_UILayoutGuide _setConstraintsToRemoveAtRuntime:];
-[_UILayoutGuide encodeWithCoder:];
-[_UILayoutGuide _setUpCounterDimensionConstraint];
-[_UILayoutGuide _layoutVariablesWithAmbiguousValue];
-[_UILayoutGuide initWithCoder:];
-[_UILayoutGuide _setHorizontal:];
-[_UILayoutGuide initWithFrame:];
-[_UILayoutGuide isHorizontal];
-[_UILayoutGuide _allowsArchivingAsSubview];
-[_UILayoutGuide _isFloatingLayoutItem];
-[_UILayoutGuide _setAllowsArchivingAsSubview:];
```
