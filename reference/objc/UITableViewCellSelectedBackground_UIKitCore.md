# `UITableViewCellSelectedBackground`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"UIVisualEffectView" _selectionEffectsView;
B _multiselect;
q _selectionStyle;
@"UIColor" _multiselectBackgroundColor;
@"UIColor" _selectionTintColor;
@"UIColor" _noneStyleBackgroundColor;
```

## Properties

```
@property (Tq,N,V_selectionStyle) selectionStyle;
@property (T@"UIColor",&,N,V_multiselectBackgroundColor) multiselectBackgroundColor;
@property (TB,N,GisMultiselect,V_multiselect) multiselect;
@property (T@"UIColor",&,N,V_selectionTintColor) selectionTintColor;
@property (T@"NSArray",C,N) selectionEffects;
@property (T@"UIColor",&,N,V_noneStyleBackgroundColor) noneStyleBackgroundColor;
```

## Instance methods

```
-[UITableViewCellSelectedBackground updateBackgroundColor];
-[UITableViewCellSelectedBackground setSelectionStyle:];
-[UITableViewCellSelectedBackground setMultiselectBackgroundColor:];
-[UITableViewCellSelectedBackground layoutSubviews];
-[UITableViewCellSelectedBackground selectionStyle];
-[UITableViewCellSelectedBackground isMultiselect];
-[UITableViewCellSelectedBackground noneStyleBackgroundColor];
-[UITableViewCellSelectedBackground setNoneStyleBackgroundColor:];
-[UITableViewCellSelectedBackground tintColorDidChange];
-[UITableViewCellSelectedBackground multiselectBackgroundColor];
-[UITableViewCellSelectedBackground setSelectionTintColor:];
-[UITableViewCellSelectedBackground selectionTintColor];
-[UITableViewCellSelectedBackground setMultiselect:];
-[UITableViewCellSelectedBackground selectionEffects];
-[UITableViewCellSelectedBackground setSelectionEffects:];
```
