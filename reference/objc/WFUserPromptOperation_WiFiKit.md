# `WFUserPromptOperation`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFOperation`
- 5 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
q _result;
@"NSDictionary" _userResponse;
@"NSDictionary" _options;
d _timeout;
Q _flags;
```

## Properties

```
@property (Tq,N,V_result) result;
@property (T@"NSDictionary",&,N,V_options) options;
@property (Td,N,V_timeout) timeout;
@property (TQ,N,V_flags) flags;
@property (T@"NSDictionary",R,N,V_userResponse) userResponse;
```

## Class methods

```
+[WFUserPromptOperation sharedMapTable];
```

## Instance methods

```
-[WFUserPromptOperation setResult:];
-[WFUserPromptOperation setOptions:];
-[WFUserPromptOperation setFlags:];
-[WFUserPromptOperation flags];
-[WFUserPromptOperation start];
-[WFUserPromptOperation timeout];
-[WFUserPromptOperation result];
-[WFUserPromptOperation setTimeout:];
-[WFUserPromptOperation options];
-[WFUserPromptOperation userResponse];
-[WFUserPromptOperation _notification:didFinishWithResponse:];
-[WFUserPromptOperation _showPrompt];
-[WFUserPromptOperation initWithOptions:timeout:];
-[WFUserPromptOperation initWithOptions:timeout:flags:];
```
