# `_UIContextMenuLayoutArbiterInput`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 16 properties, 34 instance methods, 0 class methods

## Instance variables

```
B _shouldUpdateAttachment;
B _shouldAvoidInputViews;
B _shouldConcealMenu;
B _shouldMenuOverlapSourcePreview;
d _maximumMenuHeight;
d _preferredContentSpacing;
d _additionalAlignmentOffset;
Q _preferredPreviewFittingStrategy;
@"UITargetedPreview" _sourcePreview;
@"NSArray" _accessoryViews;
@? _computePreferredScrollTruncationDetentForHeight;
{CGSize="width"d"height"d} _preferredPreviewSize;
{CGSize="width"d"height"d} _preferredMenuSize;
{CGPoint="x"d"y"d} _preferredMenuAttachmentPoint;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _preferredEdgeInsets;
{?="attachment"Q"alignment"Q"attachmentOffset"d"alignmentOffset"d"gravity"q} _preferredAnchor;
```

## Properties

```
@property (TB,N,V_shouldUpdateAttachment) shouldUpdateAttachment;
@property (TB,N,V_shouldAvoidInputViews) shouldAvoidInputViews;
@property (TB,N,V_shouldConcealMenu) shouldConcealMenu;
@property (TB,N,V_shouldMenuOverlapSourcePreview) shouldMenuOverlapSourcePreview;
@property (T{CGSize=dd},N,V_preferredPreviewSize) preferredPreviewSize;
@property (T{CGSize=dd},N,V_preferredMenuSize) preferredMenuSize;
@property (Td,N,V_maximumMenuHeight) maximumMenuHeight;
@property (T{CGPoint=dd},N,V_preferredMenuAttachmentPoint) preferredMenuAttachmentPoint;
@property (T{UIEdgeInsets=dddd},N,V_preferredEdgeInsets) preferredEdgeInsets;
@property (Td,N,V_preferredContentSpacing) preferredContentSpacing;
@property (Td,N,V_additionalAlignmentOffset) additionalAlignmentOffset;
@property (T{?=QQddq},N,V_preferredAnchor) preferredAnchor;
@property (TQ,N,V_preferredPreviewFittingStrategy) preferredPreviewFittingStrategy;
@property (T@"UITargetedPreview",&,N,V_sourcePreview) sourcePreview;
@property (T@"NSArray",&,N,V_accessoryViews) accessoryViews;
@property (T@?,C,N,V_computePreferredScrollTruncationDetentForHeight) computePreferredScrollTruncationDetentForHeight;
```

## Instance methods

```
-[_UIContextMenuLayoutArbiterInput shouldMenuOverlapSourcePreview];
-[_UIContextMenuLayoutArbiterInput setShouldMenuOverlapSourcePreview:];
-[_UIContextMenuLayoutArbiterInput setPreferredMenuSize:];
-[_UIContextMenuLayoutArbiterInput _hasVisibleMenu];
-[_UIContextMenuLayoutArbiterInput init];
-[_UIContextMenuLayoutArbiterInput sourcePreview];
-[_UIContextMenuLayoutArbiterInput preferredAnchor];
-[_UIContextMenuLayoutArbiterInput shouldAvoidInputViews];
-[_UIContextMenuLayoutArbiterInput computePreferredScrollTruncationDetentForHeight];
-[_UIContextMenuLayoutArbiterInput preferredPreviewFittingStrategy];
-[_UIContextMenuLayoutArbiterInput preferredMenuAttachmentPoint];
-[_UIContextMenuLayoutArbiterInput setAccessoryViews:];
-[_UIContextMenuLayoutArbiterInput setPreferredPreviewFittingStrategy:];
-[_UIContextMenuLayoutArbiterInput setAdditionalAlignmentOffset:];
-[_UIContextMenuLayoutArbiterInput shouldUpdateAttachment];
-[_UIContextMenuLayoutArbiterInput accessoryViews];
-[_UIContextMenuLayoutArbiterInput preferredEdgeInsets];
-[_UIContextMenuLayoutArbiterInput setMaximumMenuHeight:];
-[_UIContextMenuLayoutArbiterInput preferredMenuSize];
-[_UIContextMenuLayoutArbiterInput setPreferredAnchor:];
-[_UIContextMenuLayoutArbiterInput preferredPreviewSize];
-[_UIContextMenuLayoutArbiterInput setSourcePreview:];
-[_UIContextMenuLayoutArbiterInput shouldConcealMenu];
-[_UIContextMenuLayoutArbiterInput additionalAlignmentOffset];
-[_UIContextMenuLayoutArbiterInput setShouldUpdateAttachment:];
-[_UIContextMenuLayoutArbiterInput maximumMenuHeight];
-[_UIContextMenuLayoutArbiterInput setPreferredEdgeInsets:];
-[_UIContextMenuLayoutArbiterInput setPreferredPreviewSize:];
-[_UIContextMenuLayoutArbiterInput preferredContentSpacing];
-[_UIContextMenuLayoutArbiterInput setComputePreferredScrollTruncationDetentForHeight:];
-[_UIContextMenuLayoutArbiterInput setShouldConcealMenu:];
-[_UIContextMenuLayoutArbiterInput setPreferredContentSpacing:];
-[_UIContextMenuLayoutArbiterInput setShouldAvoidInputViews:];
-[_UIContextMenuLayoutArbiterInput setPreferredMenuAttachmentPoint:];
```
