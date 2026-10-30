# `_UIBarCustomizationSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"<_UIBarCustomizerAnimating>" _beginAnimationCoordinator;
@"<_UIBarCustomizerAnimating>" _endAnimationCoordinator;
@"NSArray" _sourceItems;
@"NSMutableArray" __mutableVisibleItems;
@"NSMutableArray" __mutableAdditionalItems;
```

## Properties

```
@property (T@"NSArray",C,N,V_sourceItems) sourceItems;
@property (T@"NSMutableArray",&,N,G_mutableVisibleItems,V__mutableVisibleItems) _mutableVisibleItems;
@property (T@"NSMutableArray",&,N,G_mutableAdditionalItems,V__mutableAdditionalItems) _mutableAdditionalItems;
@property (T@"NSArray",R,N) visibleItems;
@property (T@"NSArray",R,N) additionalItems;
@property (T@"<_UIBarCustomizerAnimating>",R,N,V_beginAnimationCoordinator) beginAnimationCoordinator;
@property (T@"<_UIBarCustomizerAnimating>",R,N,V_endAnimationCoordinator) endAnimationCoordinator;
```

## Class methods

```
+[_UIBarCustomizationSession sessionWithVisibleItems:additionalItems:];
```

## Instance methods

```
-[_UIBarCustomizationSession additionalItems];
-[_UIBarCustomizationSession visibleItems];
-[_UIBarCustomizationSession setSourceItems:];
-[_UIBarCustomizationSession _mutableAdditionalItems];
-[_UIBarCustomizationSession _mutableVisibleItems];
-[_UIBarCustomizationSession beginAnimationCoordinator];
-[_UIBarCustomizationSession endAnimationCoordinator];
-[_UIBarCustomizationSession set_mutableAdditionalItems:];
-[_UIBarCustomizationSession set_mutableVisibleItems:];
-[_UIBarCustomizationSession sourceItems];
```
