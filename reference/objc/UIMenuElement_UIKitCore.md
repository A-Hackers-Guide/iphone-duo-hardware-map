# `UIMenuElement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 11 instance variables, 16 properties, 46 instance methods, 1 class methods

## Instance variables

```
@"NSAttributedString" _attributedTitle;
@"NSString" _subtitle;
@"NSString" _accessibilityIdentifier;
Q __preferredDisplayMode;
q _preferredImageVisibility;
@"_UITextStyleDescriptor" _titleStyleDescriptor;
@"NSString" _title;
@? _highlightStateUpdateHandler;
@"NSString" __internalIdentifier;
@"<_UIMenuImageOrName>" __imageOrName;
@"UIAction" __accessoryAction;
```

## Properties

```
@property (T@"NSString",C,N,V__internalIdentifier) _internalIdentifier;
@property (TB,R,N) _isLeaf;
@property (TB,R,N) _isLoadingPlaceholder;
@property (TB,R,N) _isIntelligentAssistantAction;
@property (T@"<_UIMenuImageOrName>",R,N,V__imageOrName) _imageOrName;
@property (T@"_UITextStyleDescriptor",C,N,V_titleStyleDescriptor) _titleStyleDescriptor;
@property (TQ,N,S_setPreferredDisplayMode:,V__preferredDisplayMode) _preferredDisplayMode;
@property (T@"NSAttributedString",C,N,V_attributedTitle) attributedTitle;
@property (T@"UIAction",C,N,S_setAccessoryAction:,V__accessoryAction) _accessoryAction;
@property (T@?,C,N,S_setHighlightStateUpdateHandler:) _highlightStateUpdateHandler;
@property (Tq,N,S_setPreferredImageVisibility:) _preferredImageVisibility;
@property (T@"NSString",R,N,V_title) title;
@property (T@"NSString",C,N,V_subtitle) subtitle;
@property (T@"UIImage",R,N) image;
@property (Tq,N,V_preferredImageVisibility) preferredImageVisibility;
@property (T@?,C,N,V_highlightStateUpdateHandler) highlightStateUpdateHandler;
```

## Class methods

```
+[UIMenuElement supportsSecureCoding];
```

## Instance methods

```
-[UIMenuElement _isVisible];
-[UIMenuElement subtitle];
-[UIMenuElement _setImage:];
-[UIMenuElement setAttributedTitle:];
-[UIMenuElement _isIntelligentAssistantAction];
-[UIMenuElement set_internalIdentifier:];
-[UIMenuElement setSubtitle:];
-[UIMenuElement setAccessibilityIdentifier:];
-[UIMenuElement accessibilityIdentifier];
-[UIMenuElement title];
-[UIMenuElement _internalIdentifier];
-[UIMenuElement attributedTitle];
-[UIMenuElement encodeWithCoder:];
-[UIMenuElement initWithCoder:];
-[UIMenuElement image];
-[UIMenuElement copyWithZone:];
-[UIMenuElement preferredImageVisibility];
-[UIMenuElement _setTitle:];
-[UIMenuElement setPreferredImageVisibility:];
-[UIMenuElement _setSubtitle:];
-[UIMenuElement _acceptMenuVisit:commandVisit:actionVisit:deferredElementVisit:];
-[UIMenuElement _isLeaf];
-[UIMenuElement setHighlightStateUpdateHandler:];
-[UIMenuElement _acceptBoolMenuVisit:leafVisit:];
-[UIMenuElement _acceptBoolMenuVisit:commandVisit:actionVisit:];
-[UIMenuElement _acceptMenuVisit:leafVisit:];
-[UIMenuElement _accessoryAction];
-[UIMenuElement _canBeHighlighted];
-[UIMenuElement _customContentView];
-[UIMenuElement _highlightStateUpdateHandler];
-[UIMenuElement _imageOrName];
-[UIMenuElement _isInlineGroup];
-[UIMenuElement _isLoadingPlaceholder];
-[UIMenuElement _omitsInlineTitle];
-[UIMenuElement _preferredDisplayMode];
-[UIMenuElement _preferredImageVisibility];
-[UIMenuElement _safeCopy];
-[UIMenuElement _setAccessoryAction:];
-[UIMenuElement _setHighlightStateUpdateHandler:];
-[UIMenuElement _setPreferredDisplayMode:];
-[UIMenuElement _setPreferredImageVisibility:];
-[UIMenuElement _titleStyleDescriptor];
-[UIMenuElement _willBePreparedForInitialDisplay:];
-[UIMenuElement highlightStateUpdateHandler];
-[UIMenuElement initWithTitle:image:imageName:];
-[UIMenuElement set_titleStyleDescriptor:];
```
