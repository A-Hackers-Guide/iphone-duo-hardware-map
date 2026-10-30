# `_UINavigationBarTitleControl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `_UITAMICAdaptorViewDelegate`
- 26 instance variables, 24 properties, 73 instance methods, 1 class methods

## Instance variables

```
@"UIView" _backgroundView;
@"UILabel" _inlineTitleView;
@"_UITAMICAdaptorView" _wrapperView;
@"NSDictionary" _resolvedAttributes;
@"UIImageView" _chevron;
@"UILayoutGuide" _chevronGuide;
@"NSLayoutConstraint" _sosConstraint;
@"NSArray" _backgroundViewConstraints;
@"NSArray" _titleConstraints;
@"NSArray" _inlineTitleConstraints;
@"NSArray" _chevronConstraints;
{?="supportsTwoLineTitles"b1"adjustedTitleAttributesForTitleLength"b1"isUpdatingConstraints"b1"titleLabelAdjustsFontSizeToFitWidth"b1} _titleControlFlags;
f _titleViewCompressionResistancePriority;
@"NSAttributedString" _attributedTitle;
@"NSDictionary" _titleAttributes;
@"UIView" _titleView;
d _contentAlpha;
d _controlAlpha;
d _titleLabelMinimumScaleFactor;
@"UIView" _effectiveTitleView;
@? _titleMenuProvider;
@"UIDocumentProperties" _documentProperties;
@"UILayoutGuide" _titleLayoutGuide;
@"<_UINavigationBarTitleControlVisualProvider>" _visualProvider;
@? _intrinsicContentSizeInvalidationHandler;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _menuAlignmentInsets;
```

## Properties

```
@property (T@"NSString",C,N) title;
@property (T@"NSAttributedString",C,N,V_attributedTitle) attributedTitle;
@property (T@"NSDictionary",C,N,V_titleAttributes) titleAttributes;
@property (T@"UIView",&,N,V_titleView) titleView;
@property (Tf,N,V_titleViewCompressionResistancePriority) titleViewCompressionResistancePriority;
@property (Td,N,V_contentAlpha) contentAlpha;
@property (Td,N,V_controlAlpha) controlAlpha;
@property (TB,N) titleLabelAdjustsFontSizeToFitWidth;
@property (Td,N,V_titleLabelMinimumScaleFactor) titleLabelMinimumScaleFactor;
@property (T@"UILabel",R,N) titleLabel;
@property (T@"UIView",R,N,V_effectiveTitleView) effectiveTitleView;
@property (TB,R,N) hasBaseline;
@property (TB,R,N) isInteractive;
@property (Td,R,N) trailingPadding;
@property (T@?,C,N,V_titleMenuProvider) titleMenuProvider;
@property (T@"UIDocumentProperties",&,N,V_documentProperties) documentProperties;
@property (T{UIEdgeInsets=dddd},N,V_menuAlignmentInsets) menuAlignmentInsets;
@property (T@"UILayoutGuide",&,N,V_titleLayoutGuide) titleLayoutGuide;
@property (T@"<_UINavigationBarTitleControlVisualProvider>",&,N,V_visualProvider) visualProvider;
@property (T@?,C,N,V_intrinsicContentSizeInvalidationHandler) intrinsicContentSizeInvalidationHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UINavigationBarTitleControl titleMenuSuggestedActionsWithDocumentFileURL:];
```

## Instance methods

```
-[_UINavigationBarTitleControl _controlEventsForActionTriggered];
-[_UINavigationBarTitleControl documentProperties];
-[_UINavigationBarTitleControl titleMenuProvider];
-[_UINavigationBarTitleControl setTitleAttributes:];
-[_UINavigationBarTitleControl titleAttributes];
-[_UINavigationBarTitleControl setDocumentProperties:];
-[_UINavigationBarTitleControl setTitleMenuProvider:];
-[_UINavigationBarTitleControl visualProvider];
-[_UINavigationBarTitleControl setTitleView:];
-[_UINavigationBarTitleControl didMoveToWindow];
-[_UINavigationBarTitleControl _updateContentAlpha];
-[_UINavigationBarTitleControl _intrinsicContentSizeInvalidatedForChildView:];
-[_UINavigationBarTitleControl contextMenuInteraction:previewForDismissingMenuWithConfiguration:];
-[_UINavigationBarTitleControl intrinsicContentSizeInvalidationHandler];
-[_UINavigationBarTitleControl _preview];
-[_UINavigationBarTitleControl pointerShapeInContainer:];
-[_UINavigationBarTitleControl contentAlpha];
-[_UINavigationBarTitleControl hasBaseline];
-[_UINavigationBarTitleControl pointerInteraction:styleForRegion:];
-[_UINavigationBarTitleControl contextMenuInteraction:configurationForMenuAtLocation:];
-[_UINavigationBarTitleControl invalidateIntrinsicContentSize];
-[_UINavigationBarTitleControl setTitleLayoutGuide:];
-[_UINavigationBarTitleControl setTitleLabelAdjustsFontSizeToFitWidth:];
-[_UINavigationBarTitleControl titleLabel];
-[_UINavigationBarTitleControl pointerInteraction:willEnterRegion:animator:];
-[_UINavigationBarTitleControl pointerInteraction:willExitRegion:animator:];
-[_UINavigationBarTitleControl setContentAlpha:];
-[_UINavigationBarTitleControl isInteractive];
-[_UINavigationBarTitleControl setAttributedTitle:];
-[_UINavigationBarTitleControl setTitleAttributes:titleMenuProvider:documentProperties:titleView:attributedTitle:];
-[_UINavigationBarTitleControl _updateControlAlpha];
-[_UINavigationBarTitleControl contextMenuInteraction:previewForHighlightingMenuWithConfiguration:];
-[_UINavigationBarTitleControl availableSizeForAdaptor:proposedSize:];
-[_UINavigationBarTitleControl controlAlpha];
-[_UINavigationBarTitleControl _ensureNecessaryViews];
-[_UINavigationBarTitleControl menuAttachmentPointForConfiguration:];
-[_UINavigationBarTitleControl viewForLastBaselineLayout];
-[_UINavigationBarTitleControl layoutSubviews];
-[_UINavigationBarTitleControl effectiveTitleView];
-[_UINavigationBarTitleControl _debugInfo];
-[_UINavigationBarTitleControl _invalidateSceneDraggingBehavior];
-[_UINavigationBarTitleControl setMenuAlignmentInsets:];
-[_UINavigationBarTitleControl _preferredSender];
-[_UINavigationBarTitleControl titleLabelAdjustsFontSizeToFitWidth];
-[_UINavigationBarTitleControl setHighlighted:];
-[_UINavigationBarTitleControl title];
-[_UINavigationBarTitleControl titleViewCompressionResistancePriority];
-[_UINavigationBarTitleControl viewForFirstBaselineLayout];
-[_UINavigationBarTitleControl _baselineView];
-[_UINavigationBarTitleControl setTitleLabelMinimumScaleFactor:];
-[_UINavigationBarTitleControl attributedTitle];
-[_UINavigationBarTitleControl pointerInteraction:regionForRequest:defaultRegion:];
-[_UINavigationBarTitleControl _resetTitleViewConstraints];
-[_UINavigationBarTitleControl setVisualProvider:];
-[_UINavigationBarTitleControl updateConstraints];
-[_UINavigationBarTitleControl setIntrinsicContentSizeInvalidationHandler:];
-[_UINavigationBarTitleControl setTitle:];
-[_UINavigationBarTitleControl titleView];
-[_UINavigationBarTitleControl _inactiveForPointer];
-[_UINavigationBarTitleControl _updateInteractions];
-[_UINavigationBarTitleControl setControlAlpha:];
-[_UINavigationBarTitleControl _preferredPresentationSourceItem];
-[_UINavigationBarTitleControl _cleanupWrapperView];
-[_UINavigationBarTitleControl _backgroundViewConstraintsForIdiom:];
-[_UINavigationBarTitleControl initWithFrame:];
-[_UINavigationBarTitleControl menuAlignmentInsets];
-[_UINavigationBarTitleControl trailingPadding];
-[_UINavigationBarTitleControl _updateInlineTitleView];
-[_UINavigationBarTitleControl _contextMenuInteraction:styleForMenuWithConfiguration:];
-[_UINavigationBarTitleControl titleLabelMinimumScaleFactor];
-[_UINavigationBarTitleControl titleLayoutGuide];
-[_UINavigationBarTitleControl _contextMenuInteraction:overrideSuggestedActionsForConfiguration:];
-[_UINavigationBarTitleControl setTitleViewCompressionResistancePriority:];
```
