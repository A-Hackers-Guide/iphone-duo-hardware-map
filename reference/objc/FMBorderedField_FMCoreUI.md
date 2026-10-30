# `FMBorderedField`

- Image: [`/System/Library/PrivateFrameworks/FMCoreUI.framework/FMCoreUI`](../userland/System__Library__PrivateFrameworks__FMCoreUI.framework__FMCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _isConfigured;
@"UIColor" _borderColor;
@"FMHorizontalRule" _topRule;
@"FMHorizontalRule" _bottomRule;
```

## Properties

```
@property (TB,N,V_isConfigured) isConfigured;
@property (T@"FMHorizontalRule",&,N,V_topRule) topRule;
@property (T@"FMHorizontalRule",&,N,V_bottomRule) bottomRule;
@property (T@"UIColor",&,N,V_borderColor) borderColor;
```

## Class methods

```
+[FMBorderedField requiresConstraintBasedLayout];
```

## Instance methods

```
-[FMBorderedField setBorderColor:];
-[FMBorderedField initWithCoder:];
-[FMBorderedField initWithFrame:];
-[FMBorderedField borderColor];
-[FMBorderedField awakeFromNib];
-[FMBorderedField prepareForInterfaceBuilder];
-[FMBorderedField isConfigured];
-[FMBorderedField setIsConfigured:];
-[FMBorderedField topRule];
-[FMBorderedField bottomRule];
-[FMBorderedField commonSetup];
-[FMBorderedField setBottomRule:];
-[FMBorderedField setTopRule:];
```
