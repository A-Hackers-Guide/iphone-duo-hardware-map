# `_UICampoActionConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`
- 7 instance variables, 11 properties, 20 instance methods, 0 class methods

## Instance variables

```
q _assistantType;
q _presenterSource;
@"_UIIntelligentAssistantTextSelectionContext" _textSelectionContext;
@"_UIIntelligentAssistantImageSelectionContext" _imageSelectionContext;
@"NSString" _initialLightweightState;
q _initialLightweightLayout;
@"NSString" _sessionIdentifier;
```

## Properties

```
@property (T@"_UIIntelligentAssistantTextSelectionContext",&,N,S_setTextSelectionContext:,V_textSelectionContext) _textSelectionContext;
@property (T@"_UIIntelligentAssistantImageSelectionContext",&,N,S_setImageSelectionContext:,V_imageSelectionContext) _imageSelectionContext;
@property (T@"NSString",C,N,S_setInitialLightweightState:,V_initialLightweightState) _initialLightweightState;
@property (Tq,N,S_setInitialLightweightLayout:,V_initialLightweightLayout) _initialLightweightLayout;
@property (T@"NSString",C,N,V_sessionIdentifier) sessionIdentifier;
@property (Tq,N,S_setPresenterSource:,V_presenterSource) _presenterSource;
@property (Tq,N,S_setAssistantType:,V_assistantType) _assistantType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICampoActionConfiguration sessionIdentifier];
-[_UICampoActionConfiguration debugDescription];
-[_UICampoActionConfiguration init];
-[_UICampoActionConfiguration setSessionIdentifier:];
-[_UICampoActionConfiguration description];
-[_UICampoActionConfiguration appendDescriptionToStream:];
-[_UICampoActionConfiguration copyWithZone:];
-[_UICampoActionConfiguration _applyValuesFromConfiguration:];
-[_UICampoActionConfiguration _assistantType];
-[_UICampoActionConfiguration _imageSelectionContext];
-[_UICampoActionConfiguration _initialLightweightLayout];
-[_UICampoActionConfiguration _initialLightweightState];
-[_UICampoActionConfiguration _presenterSource];
-[_UICampoActionConfiguration _setAssistantType:];
-[_UICampoActionConfiguration _setImageSelectionContext:];
-[_UICampoActionConfiguration _setInitialLightweightLayout:];
-[_UICampoActionConfiguration _setInitialLightweightState:];
-[_UICampoActionConfiguration _setPresenterSource:];
-[_UICampoActionConfiguration _setTextSelectionContext:];
-[_UICampoActionConfiguration _textSelectionContext];
```
