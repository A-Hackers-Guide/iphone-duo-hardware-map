# `_UISheetPresentationControllerAppearance`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`, `NSSecureCoding`
- 3 instance variables, 8 properties, 10 instance methods, 5 class methods

## Instance variables

```
B __prefersDimmingVisible;
@"NSString" __largestUndimmedDetentIdentifier;
@"NSString" __smallestDimmedDetentIdentifier;
```

## Properties

```
@property (TB,R,N,G_isDimmingAlwaysVisible) _dimmingAlwaysVisible;
@property (TB,R,N,V__prefersDimmingVisible) _prefersDimmingVisible;
@property (T@"NSString",R,N,V__largestUndimmedDetentIdentifier) _largestUndimmedDetentIdentifier;
@property (T@"NSString",R,N,V__smallestDimmedDetentIdentifier) _smallestDimmedDetentIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISheetPresentationControllerAppearance supportsBSXPCSecureCoding];
+[_UISheetPresentationControllerAppearance supportsSecureCoding];
+[_UISheetPresentationControllerAppearance appearanceWithSmallestDimmedDetentIdentifier:];
+[_UISheetPresentationControllerAppearance appearanceWithLargestUndimmedDetentIdentifier:];
+[_UISheetPresentationControllerAppearance appearancePreferringDimmingVisible:];
```

## Instance methods

```
-[_UISheetPresentationControllerAppearance _smallestDimmedDetentIdentifier];
-[_UISheetPresentationControllerAppearance _isDimmingAlwaysVisible];
-[_UISheetPresentationControllerAppearance encodeWithCoder:];
-[_UISheetPresentationControllerAppearance description];
-[_UISheetPresentationControllerAppearance initWithCoder:];
-[_UISheetPresentationControllerAppearance encodeWithBSXPCCoder:];
-[_UISheetPresentationControllerAppearance initWithBSXPCCoder:];
-[_UISheetPresentationControllerAppearance _prefersDimmingVisible];
-[_UISheetPresentationControllerAppearance isEqual:];
-[_UISheetPresentationControllerAppearance _largestUndimmedDetentIdentifier];
```
