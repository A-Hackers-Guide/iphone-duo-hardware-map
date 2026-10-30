# `_UIIntelligentAssistantAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIAction`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"<UIPopoverPresentationControllerSourceItem>" _overridePresentationSourceItem;
@"<_UICampoServiceSessionDelegate>" __sessionDelegate;
@"_UICampoActionConfiguration" __presenterConfiguration;
```

## Properties

```
@property (T@"<_UICampoServiceSessionDelegate>",W,N,S_setSessionDelegate:,V__sessionDelegate) _sessionDelegate;
@property (T@"<UIPopoverPresentationControllerSourceItem>",W,N,S_setOverridePresentationSourceItem:,V_overridePresentationSourceItem) _overridePresentationSourceItem;
@property (T@"_UICampoActionConfiguration",C,N,S_setPresenterConfiguration:,V__presenterConfiguration) _presenterConfiguration;
```

## Class methods

```
+[_UIIntelligentAssistantAction actionWithIdentifier:configurationProvider:];
```

## Instance methods

```
-[_UIIntelligentAssistantAction initWithIdentifier:configurationProvider:];
-[_UIIntelligentAssistantAction _sessionDelegate];
-[_UIIntelligentAssistantAction _isIntelligentAssistantAction];
-[_UIIntelligentAssistantAction keepsMenuPresented];
-[_UIIntelligentAssistantAction _setPresenterConfiguration:];
-[_UIIntelligentAssistantAction _presenterConfiguration];
-[_UIIntelligentAssistantAction _overridePresentationSourceItem];
-[_UIIntelligentAssistantAction copyWithZone:];
-[_UIIntelligentAssistantAction _setOverridePresentationSourceItem:];
-[_UIIntelligentAssistantAction _setSessionDelegate:];
```
