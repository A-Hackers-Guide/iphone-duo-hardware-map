# `_UIMainMenuSessionRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 7 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"_UIMainMenuSession" _providedSessionToEnd;
B _beginNewSession;
B _includeUncategorizedMenuState;
B _requiresHostSideInvokableKeyboardShortcuts;
@"_UIMainMenuSessionIdentifier" _sessionIdentifierToEnd;
@"NSSet" _initialMenuStateIdentifiers;
```

## Properties

```
@property (T@"_UIMainMenuSessionIdentifier",R,N,V_sessionIdentifierToEnd) _sessionIdentifierToEnd;
@property (TB,N,V_beginNewSession) beginNewSession;
@property (T@"_UIMainMenuSession",&,N) sessionToEnd;
@property (T@"_UIMainMenuIdentifier",&,N) initialMenuStateIdentifier;
@property (T@"NSSet",&,N,V_initialMenuStateIdentifiers) initialMenuStateIdentifiers;
@property (TB,N,V_includeUncategorizedMenuState) includeUncategorizedMenuState;
@property (TB,N,V_requiresHostSideInvokableKeyboardShortcuts) requiresHostSideInvokableKeyboardShortcuts;
```

## Class methods

```
+[_UIMainMenuSessionRequest supportsSecureCoding];
```

## Instance methods

```
-[_UIMainMenuSessionRequest init];
-[_UIMainMenuSessionRequest encodeWithCoder:];
-[_UIMainMenuSessionRequest hash];
-[_UIMainMenuSessionRequest description];
-[_UIMainMenuSessionRequest initWithCoder:];
-[_UIMainMenuSessionRequest isEqual:];
-[_UIMainMenuSessionRequest setInitialMenuStateIdentifiers:];
-[_UIMainMenuSessionRequest beginNewSession];
-[_UIMainMenuSessionRequest _sessionIdentifierToEnd];
-[_UIMainMenuSessionRequest includeUncategorizedMenuState];
-[_UIMainMenuSessionRequest initialMenuStateIdentifier];
-[_UIMainMenuSessionRequest initialMenuStateIdentifiers];
-[_UIMainMenuSessionRequest requiresHostSideInvokableKeyboardShortcuts];
-[_UIMainMenuSessionRequest sessionToEnd];
-[_UIMainMenuSessionRequest setBeginNewSession:];
-[_UIMainMenuSessionRequest setIncludeUncategorizedMenuState:];
-[_UIMainMenuSessionRequest setInitialMenuStateIdentifier:];
-[_UIMainMenuSessionRequest setRequiresHostSideInvokableKeyboardShortcuts:];
-[_UIMainMenuSessionRequest setSessionToEnd:];
```
