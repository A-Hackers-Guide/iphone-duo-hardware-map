# `UICustomViewMenuElement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIMenuElement`
- Protocols: `_UIMenuLeaf`, `UIMenuLeaf`
- 9 instance variables, 32 properties, 45 instance methods, 1 class methods

## Instance variables

```
B _forceCustomViewSupport;
Q attributes;
@"NSString" discoverabilityTitle;
q state;
@ _sender;
@"UIImage" _selectedImage;
@"UIMenuElement" _menuElementRepresentation;
@? _primaryActionHandler;
@? _viewProvider;
```

## Properties

```
@property (T@?,C,N,V_viewProvider) viewProvider;
@property (TB,N,S_setForceCustomViewSupport:,V_forceCustomViewSupport) _forceCustomViewSupport;
@property (T@"UIView",R,N) contentView;
@property (T@"UIMenuElement",&,N,V_menuElementRepresentation) menuElementRepresentation;
@property (T@?,C,N,V_primaryActionHandler) primaryActionHandler;
@property (T@"NSAttributedString",C,N) attributedTitle;
@property (TB,R,N) keepsMenuPresented;
@property (T@"_UITextStyleDescriptor",C,N) _titleStyleDescriptor;
@property (T@"UISPasteVariant",R,N) _pasteVariant;
@property (T@"<UISSecureVariant>",R,N) _secureVariant;
@property (T@"NSArray",C,N,S_setLeafAlternates:) _leafAlternates;
@property (T@"_UIMenuLeafKeyboardShortcut",R,N) _keyboardShortcut;
@property (Tq,N,S_setEnumerationPriority:) _enumerationPriority;
@property (T@"BKSHIDEventDeferringEnvironment",R,N) _eventDeferringEnvironment;
@property (TB,N,S_setAllowsGlobeKeyModifier:) _allowsGlobeKeyModifier;
@property (TB,R,N) _isIntelligentAssistantAction;
@property (T@"<UIPopoverPresentationControllerSourceItem>",?,W,N,S_setOverridePresentationSourceItem:) _overridePresentationSourceItem;
@property (T@"NSString",C,N) title;
@property (T@"NSString",C,N) subtitle;
@property (T@"UIImage",C,N) image;
@property (T@"UIImage",C,N,V_selectedImage) selectedImage;
@property (Tq,N) preferredImageVisibility;
@property (T@"NSString",C,N,VdiscoverabilityTitle) discoverabilityTitle;
@property (TQ,N,Vattributes) attributes;
@property (Tq,N,Vstate) state;
@property (Tq,N) repeatBehavior;
@property (T@,R,N,V_sender) sender;
@property (T@"<UIPopoverPresentationControllerSourceItem>",R,N) presentationSourceItem;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UICustomViewMenuElement elementWithViewProvider:];
```

## Instance methods

```
-[UICustomViewMenuElement setViewProvider:];
-[UICustomViewMenuElement setState:];
-[UICustomViewMenuElement viewProvider];
-[UICustomViewMenuElement setAttributes:];
-[UICustomViewMenuElement keepsMenuPresented];
-[UICustomViewMenuElement sender];
-[UICustomViewMenuElement selectedImage];
-[UICustomViewMenuElement encodeWithCoder:];
-[UICustomViewMenuElement contentView];
-[UICustomViewMenuElement attributes];
-[UICustomViewMenuElement setSelectedImage:];
-[UICustomViewMenuElement state];
-[UICustomViewMenuElement _acceptMenuVisit:commandVisit:actionVisit:deferredElementVisit:];
-[UICustomViewMenuElement _isLeaf];
-[UICustomViewMenuElement _acceptBoolMenuVisit:leafVisit:];
-[UICustomViewMenuElement _leafAlternates];
-[UICustomViewMenuElement _acceptBoolMenuVisit:commandVisit:actionVisit:];
-[UICustomViewMenuElement _acceptMenuVisit:leafVisit:];
-[UICustomViewMenuElement _allowsGlobeKeyModifier];
-[UICustomViewMenuElement _enumerationPriority];
-[UICustomViewMenuElement _eventDeferringEnvironment];
-[UICustomViewMenuElement _forceCustomViewSupport];
-[UICustomViewMenuElement _isDefaultCommand];
-[UICustomViewMenuElement _keyboardShortcut];
-[UICustomViewMenuElement _menuLeafWithKeyboardShortcut:];
-[UICustomViewMenuElement _pasteVariant];
-[UICustomViewMenuElement _resolvedTargetFromFirstTarget:sender:];
-[UICustomViewMenuElement _secureVariant];
-[UICustomViewMenuElement _setAllowsGlobeKeyModifier:];
-[UICustomViewMenuElement _setEnumerationPriority:];
-[UICustomViewMenuElement _setForceCustomViewSupport:];
-[UICustomViewMenuElement _setLeafAlternates:];
-[UICustomViewMenuElement _validatedLeafWithTarget:validator:];
-[UICustomViewMenuElement _wantsPriorityOverSystemBehavior:];
-[UICustomViewMenuElement discoverabilityTitle];
-[UICustomViewMenuElement initWithMenuElement:];
-[UICustomViewMenuElement menuElementRepresentation];
-[UICustomViewMenuElement performWithSender:target:];
-[UICustomViewMenuElement presentationSourceItem];
-[UICustomViewMenuElement primaryActionHandler];
-[UICustomViewMenuElement repeatBehavior];
-[UICustomViewMenuElement setDiscoverabilityTitle:];
-[UICustomViewMenuElement setMenuElementRepresentation:];
-[UICustomViewMenuElement setPrimaryActionHandler:];
-[UICustomViewMenuElement setRepeatBehavior:];
```
