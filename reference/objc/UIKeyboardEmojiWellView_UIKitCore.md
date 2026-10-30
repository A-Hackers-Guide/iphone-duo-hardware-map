# `UIKeyboardEmojiWellView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIKeyboardEmojiDraggableViewDelegate`
- 12 instance variables, 16 properties, 29 instance methods, 0 class methods

## Instance variables

```
B _selected;
B _activeSelection;
B _unreleasedHighlight;
@"NSArray" _compositeImageRepresentation;
@"UIFont" _labelFont;
@"NSString" _stringRepresentation;
@"UIColor" _selectionBackgroundColor;
@"NSIndexPath" _associatedIndexPath;
@"UILabel" _unreleasedBanner;
@"UIView" _wellContentView;
@"UIView" _backgroundView;
{CGSize="width"d"height"d} _compositeImageSize;
```

## Properties

```
@property (T@"UILabel",&,N,V_unreleasedBanner) unreleasedBanner;
@property (T@"UIView",&,N,V_wellContentView) wellContentView;
@property (T@"UIView",&,N,V_backgroundView) backgroundView;
@property (T{CGSize=dd},N,V_compositeImageSize) compositeImageSize;
@property (T@"NSArray",&,N,V_compositeImageRepresentation) compositeImageRepresentation;
@property (T@"UIFont",&,N,V_labelFont) labelFont;
@property (T@"NSString",&,N,V_stringRepresentation) stringRepresentation;
@property (TB,N,GisSelected,V_selected) selected;
@property (TB,N,GisActiveSelection,V_activeSelection) activeSelection;
@property (T@"UIColor",&,N,V_selectionBackgroundColor) selectionBackgroundColor;
@property (T@"NSIndexPath",&,N,V_associatedIndexPath) associatedIndexPath;
@property (TB,N,V_unreleasedHighlight) unreleasedHighlight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKeyboardEmojiWellView setSelected:];
-[UIKeyboardEmojiWellView layoutSubviews];
-[UIKeyboardEmojiWellView stringRepresentation];
-[UIKeyboardEmojiWellView isSelected];
-[UIKeyboardEmojiWellView backgroundView];
-[UIKeyboardEmojiWellView initWithFrame:];
-[UIKeyboardEmojiWellView setBackgroundView:];
-[UIKeyboardEmojiWellView wellContentView];
-[UIKeyboardEmojiWellView associatedIndexPath];
-[UIKeyboardEmojiWellView compositeImageRepresentation];
-[UIKeyboardEmojiWellView compositeImageSize];
-[UIKeyboardEmojiWellView dragWillBegin:];
-[UIKeyboardEmojiWellView fontUsingSilhouette:size:];
-[UIKeyboardEmojiWellView isActiveSelection];
-[UIKeyboardEmojiWellView labelFont];
-[UIKeyboardEmojiWellView selectionBackgroundColor];
-[UIKeyboardEmojiWellView setActiveSelection:];
-[UIKeyboardEmojiWellView setAssociatedIndexPath:];
-[UIKeyboardEmojiWellView setCompositeImageRepresentation:];
-[UIKeyboardEmojiWellView setCompositeImageSize:];
-[UIKeyboardEmojiWellView setLabelFont:];
-[UIKeyboardEmojiWellView setSelectionBackgroundColor:];
-[UIKeyboardEmojiWellView setStringRepresentation:];
-[UIKeyboardEmojiWellView setStringRepresentation:silhouette:];
-[UIKeyboardEmojiWellView setUnreleasedBanner:];
-[UIKeyboardEmojiWellView setUnreleasedHighlight:];
-[UIKeyboardEmojiWellView setWellContentView:];
-[UIKeyboardEmojiWellView unreleasedBanner];
-[UIKeyboardEmojiWellView unreleasedHighlight];
```
