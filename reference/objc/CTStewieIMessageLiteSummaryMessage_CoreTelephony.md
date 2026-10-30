# `CTStewieIMessageLiteSummaryMessage`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTStewieMessageIncoming`
- 2 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
q _pendingIMessageLiteTotalCount;
@"NSArray" _pendingCounts;
```

## Properties

```
@property (Tq,N,V_pendingIMessageLiteTotalCount) pendingIMessageLiteTotalCount;
@property (T@"NSArray",&,N,V_pendingCounts) pendingCounts;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CTStewieIMessageLiteSummaryMessage supportsSecureCoding];
```

## Instance methods

```
-[CTStewieIMessageLiteSummaryMessage encodeWithCoder:];
-[CTStewieIMessageLiteSummaryMessage description];
-[CTStewieIMessageLiteSummaryMessage initWithCoder:];
-[CTStewieIMessageLiteSummaryMessage copyWithZone:];
-[CTStewieIMessageLiteSummaryMessage isEqual:];
-[CTStewieIMessageLiteSummaryMessage pendingCounts];
-[CTStewieIMessageLiteSummaryMessage isEqualToOther:];
-[CTStewieIMessageLiteSummaryMessage initWithPendingIMessageLiteTotalCount:pendingCounts:error:];
-[CTStewieIMessageLiteSummaryMessage pendingIMessageLiteTotalCount];
-[CTStewieIMessageLiteSummaryMessage setPendingCounts:];
-[CTStewieIMessageLiteSummaryMessage setPendingIMessageLiteTotalCount:];
```
