# `UIDeferredMenuElement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIMenuElement`
- Protocols: `_UIMenuLeaf`
- 13 instance variables, 34 properties, 47 instance methods, 7 class methods

## Instance variables

```
B _isSignalingFulfillment;
@"UIDeferredMenuElementProvider" _elementProvider;
B _cachesItems;
B _fulfilled;
Q _attributes;
@"NSString" _discoverabilityTitle;
q _state;
@ _sender;
@"UIImage" _selectedImage;
@"NSString" _identifier;
@ _metadata;
@"<UIDeferredMenuElementDelegate>" _delegate;
@"NSArray" _fulfilledElements;
```

## Properties

```
@property (T@,&,N,V_metadata) metadata;
@property (T@"<UIDeferredMenuElementDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",R,C,N,V_fulfilledElements) fulfilledElements;
@property (TB,R,N,V_fulfilled) fulfilled;
@property (TB,R,N,V_cachesItems) cachesItems;
@property (T@"NSString",R,C,N) _identifier;
@property (T@"NSString",R,C,N,V_identifier) identifier;
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
@property (T@"NSString",C,N,V_discoverabilityTitle) discoverabilityTitle;
@property (TQ,N,V_attributes) attributes;
@property (Tq,N,V_state) state;
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
+[UIDeferredMenuElement supportsSecureCoding];
+[UIDeferredMenuElement _elementWithIdentifier:cacheItems:elementProvider:];
+[UIDeferredMenuElement _elementWithIdentifier:];
+[UIDeferredMenuElement elementWithUncachedProvider:];
+[UIDeferredMenuElement elementWithProvider:];
+[UIDeferredMenuElement _uncachedElementWithIdentifier:];
+[UIDeferredMenuElement elementUsingFocusWithIdentifier:shouldCacheItems:];
```

## Instance methods

```
-[UIDeferredMenuElement setState:];
-[UIDeferredMenuElement identifier];
-[UIDeferredMenuElement setAttributes:];
-[UIDeferredMenuElement keepsMenuPresented];
-[UIDeferredMenuElement metadata];
-[UIDeferredMenuElement sender];
-[UIDeferredMenuElement setDelegate:];
-[UIDeferredMenuElement selectedImage];
-[UIDeferredMenuElement encodeWithCoder:];
-[UIDeferredMenuElement setMetadata:];
-[UIDeferredMenuElement delegate];
-[UIDeferredMenuElement description];
-[UIDeferredMenuElement initWithCoder:];
-[UIDeferredMenuElement attributes];
-[UIDeferredMenuElement setSelectedImage:];
-[UIDeferredMenuElement copyWithZone:];
-[UIDeferredMenuElement _identifier];
-[UIDeferredMenuElement state];
-[UIDeferredMenuElement _acceptMenuVisit:commandVisit:actionVisit:deferredElementVisit:];
-[UIDeferredMenuElement _isLeaf];
-[UIDeferredMenuElement _leafAlternates];
-[UIDeferredMenuElement _acceptMenuVisit:leafVisit:];
-[UIDeferredMenuElement _allowsGlobeKeyModifier];
-[UIDeferredMenuElement _enumerationPriority];
-[UIDeferredMenuElement _eventDeferringEnvironment];
-[UIDeferredMenuElement _fulfillIfNecessaryWithInitialResponder:];
-[UIDeferredMenuElement _isDefaultCommand];
-[UIDeferredMenuElement _isLoadingPlaceholder];
-[UIDeferredMenuElement _keyboardShortcut];
-[UIDeferredMenuElement _menuLeafWithKeyboardShortcut:];
-[UIDeferredMenuElement _pasteVariant];
-[UIDeferredMenuElement _resolvedTargetFromFirstTarget:sender:];
-[UIDeferredMenuElement _secureVariant];
-[UIDeferredMenuElement _setAllowsGlobeKeyModifier:];
-[UIDeferredMenuElement _setEnumerationPriority:];
-[UIDeferredMenuElement _setLeafAlternates:];
-[UIDeferredMenuElement _validatedLeafWithTarget:validator:];
-[UIDeferredMenuElement _wantsPriorityOverSystemBehavior:];
-[UIDeferredMenuElement cachesItems];
-[UIDeferredMenuElement discoverabilityTitle];
-[UIDeferredMenuElement fulfilled];
-[UIDeferredMenuElement fulfilledElements];
-[UIDeferredMenuElement performWithSender:target:];
-[UIDeferredMenuElement presentationSourceItem];
-[UIDeferredMenuElement repeatBehavior];
-[UIDeferredMenuElement setDiscoverabilityTitle:];
-[UIDeferredMenuElement setRepeatBehavior:];
```
