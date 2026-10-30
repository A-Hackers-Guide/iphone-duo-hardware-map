# `SBInvalidationDodgingModifierEventResponse`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDodgingModifierEventResponse`
- 4 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _disableCoalescing;
Q _options;
@"NSString" _completionIdentifier;
@"NSString" _identifier;
```

## Properties

```
@property (TQ,R,N,V_options) options;
@property (TB,N,V_disableCoalescing) disableCoalescing;
@property (T@"NSString",&,N,V_completionIdentifier) completionIdentifier;
@property (T@"NSString",&,N,V_identifier) identifier;
```

## Class methods

```
+[SBInvalidationDodgingModifierEventResponse responseWithOptions:];
```

## Instance methods

```
-[SBInvalidationDodgingModifierEventResponse identifier];
-[SBInvalidationDodgingModifierEventResponse initWithOptions:];
-[SBInvalidationDodgingModifierEventResponse setIdentifier:];
-[SBInvalidationDodgingModifierEventResponse type];
-[SBInvalidationDodgingModifierEventResponse description];
-[SBInvalidationDodgingModifierEventResponse options];
-[SBInvalidationDodgingModifierEventResponse completionIdentifier];
-[SBInvalidationDodgingModifierEventResponse disableCoalescing];
-[SBInvalidationDodgingModifierEventResponse setCompletionIdentifier:];
-[SBInvalidationDodgingModifierEventResponse setDisableCoalescing:];
```
