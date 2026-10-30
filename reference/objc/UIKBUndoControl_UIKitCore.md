# `UIKBUndoControl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- 10 instance variables, 10 properties, 32 instance methods, 1 class methods

## Instance variables

```
q _type;
@"UIKBUndoStyling" _style;
@"UIView" _springCoverView;
@"UILabel" _label;
@"UIImageView" _icon;
@"_UISlotView" _securePasteButtonSlotView;
@"NSLayoutConstraint" _coverConstraintLeftAnchor;
@"NSLayoutConstraint" _coverConstraintRightAnchor;
@"NSLayoutConstraint" _coverConstraintTopAnchor;
@"NSLayoutConstraint" _coverConstraintBottomAnchor;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (T@"UIKBUndoStyling",&,N,V_style) style;
@property (T@"UIView",&,N,V_springCoverView) springCoverView;
@property (T@"UILabel",&,N,V_label) label;
@property (T@"UIImageView",&,N,V_icon) icon;
@property (T@"_UISlotView",W,N,V_securePasteButtonSlotView) securePasteButtonSlotView;
@property (T@"NSLayoutConstraint",&,N,V_coverConstraintLeftAnchor) coverConstraintLeftAnchor;
@property (T@"NSLayoutConstraint",&,N,V_coverConstraintRightAnchor) coverConstraintRightAnchor;
@property (T@"NSLayoutConstraint",&,N,V_coverConstraintTopAnchor) coverConstraintTopAnchor;
@property (T@"NSLayoutConstraint",&,N,V_coverConstraintBottomAnchor) coverConstraintBottomAnchor;
```

## Class methods

```
+[UIKBUndoControl controlLableTextByType:style:available:];
```

## Instance methods

```
-[UIKBUndoControl label];
-[UIKBUndoControl setLabel:];
-[UIKBUndoControl setIcon:];
-[UIKBUndoControl viewForLastBaselineLayout];
-[UIKBUndoControl layoutSubviews];
-[UIKBUndoControl style];
-[UIKBUndoControl setStyle:];
-[UIKBUndoControl setType:];
-[UIKBUndoControl type];
-[UIKBUndoControl viewForFirstBaselineLayout];
-[UIKBUndoControl pointInside:withEvent:];
-[UIKBUndoControl icon];
-[UIKBUndoControl setCoverConstraintBottomAnchor:];
-[UIKBUndoControl springCoverView];
-[UIKBUndoControl _secureName];
-[UIKBUndoControl configureSecurePasteButtonInRootView:];
-[UIKBUndoControl controlImageByType:];
-[UIKBUndoControl controlLabelImageNameByType:isRTL:];
-[UIKBUndoControl coverConstraintBottomAnchor];
-[UIKBUndoControl coverConstraintLeftAnchor];
-[UIKBUndoControl coverConstraintRightAnchor];
-[UIKBUndoControl coverConstraintTopAnchor];
-[UIKBUndoControl initWithType:andStyling:];
-[UIKBUndoControl layoutControlForType:andStyling:];
-[UIKBUndoControl securePasteButtonSlotView];
-[UIKBUndoControl setCoverConstraintLeftAnchor:];
-[UIKBUndoControl setCoverConstraintRightAnchor:];
-[UIKBUndoControl setCoverConstraintTopAnchor:];
-[UIKBUndoControl setSecurePasteButtonSlotView:];
-[UIKBUndoControl setSpringCoverView:];
-[UIKBUndoControl updateCoverWithTavelProcess:isRTL:];
-[UIKBUndoControl updateUndoControlStyle];
```
