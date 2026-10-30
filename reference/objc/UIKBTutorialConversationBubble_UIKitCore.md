# `UIKBTutorialConversationBubble`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 11 instance variables, 13 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"CAShapeLayer" _backdropMaskShapeLayer;
@"UIKBTutorialConversationBubbleShadowLayer" _broadShadowLayer;
@"UIKBTutorialConversationBubbleShadowLayer" _tightShadowLayer;
@"UIKBTutorialConversationBubbleBackdropLayer" _backdropLayer;
@"UIView" _contentView;
q _originationDirection;
d _preferredTailAttachmentPointXCoordinate;
@"UILabel" _summaryLabel;
{CGPoint="x"d"y"d} _originationPoint;
{CGPoint="x"d"y"d} _tailAttachmentPoint;
{CGSize="width"d"height"d} _parentAvatarViewSize;
```

## Properties

```
@property (T@"CAShapeLayer",&,N,V_backdropMaskShapeLayer) backdropMaskShapeLayer;
@property (T@"UIKBTutorialConversationBubbleShadowLayer",&,N,V_broadShadowLayer) broadShadowLayer;
@property (T@"UIKBTutorialConversationBubbleShadowLayer",&,N,V_tightShadowLayer) tightShadowLayer;
@property (T@"UIKBTutorialConversationBubbleBackdropLayer",&,N,V_backdropLayer) backdropLayer;
@property (T@"UIView",R,N,V_contentView) contentView;
@property (Td,R,N) pillCornerRadius;
@property (T{UIEdgeInsets=dddd},R,N) contentViewPadding;
@property (Tq,N,V_originationDirection) originationDirection;
@property (T{CGPoint=dd},N,V_originationPoint) originationPoint;
@property (Td,N,V_preferredTailAttachmentPointXCoordinate) preferredTailAttachmentPointXCoordinate;
@property (T{CGPoint=dd},R,N,V_tailAttachmentPoint) tailAttachmentPoint;
@property (T{CGSize=dd},N,V_parentAvatarViewSize) parentAvatarViewSize;
@property (T@"UILabel",&,N,V_summaryLabel) summaryLabel;
```

## Instance methods

```
-[UIKBTutorialConversationBubble balloonCornerRadius];
-[UIKBTutorialConversationBubble intrinsicContentSize];
-[UIKBTutorialConversationBubble backdropLayer];
-[UIKBTutorialConversationBubble setBackdropLayer:];
-[UIKBTutorialConversationBubble layoutSubviews];
-[UIKBTutorialConversationBubble sizeThatFits:];
-[UIKBTutorialConversationBubble contentView];
-[UIKBTutorialConversationBubble pillCornerRadius];
-[UIKBTutorialConversationBubble tailAnchorPoint];
-[UIKBTutorialConversationBubble _pathForTailedBalloonSegmentWithStartPoint:endPoint:anchorPoint:originationDirection:];
-[UIKBTutorialConversationBubble _updateUserInterfaceStyles];
-[UIKBTutorialConversationBubble activityItemToContactItemVerticalOverlap];
-[UIKBTutorialConversationBubble backdropMaskShapeLayer];
-[UIKBTutorialConversationBubble balloonTailHeight];
-[UIKBTutorialConversationBubble balloonTailRadius];
-[UIKBTutorialConversationBubble balloonTailWidth];
-[UIKBTutorialConversationBubble broadShadowLayer];
-[UIKBTutorialConversationBubble contentViewPadding];
-[UIKBTutorialConversationBubble initWithText:originationDirection:];
-[UIKBTutorialConversationBubble originationDirection];
-[UIKBTutorialConversationBubble originationPoint];
-[UIKBTutorialConversationBubble parentAvatarViewSize];
-[UIKBTutorialConversationBubble pillRect];
-[UIKBTutorialConversationBubble preferredTailAttachmentPointXCoordinate];
-[UIKBTutorialConversationBubble setBackdropMaskShapeLayer:];
-[UIKBTutorialConversationBubble setBroadShadowLayer:];
-[UIKBTutorialConversationBubble setOriginationDirection:];
-[UIKBTutorialConversationBubble setOriginationPoint:];
-[UIKBTutorialConversationBubble setParentAvatarViewSize:];
-[UIKBTutorialConversationBubble setPreferredTailAttachmentPointXCoordinate:];
-[UIKBTutorialConversationBubble setSummaryLabel:];
-[UIKBTutorialConversationBubble setTightShadowLayer:];
-[UIKBTutorialConversationBubble summaryLabel];
-[UIKBTutorialConversationBubble tailAttachmentPoint];
-[UIKBTutorialConversationBubble tightShadowLayer];
```
