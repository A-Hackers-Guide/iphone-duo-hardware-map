# `TUMediaTokens`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 4 instance variables, 4 properties, 14 instance methods, 1 class methods

## Instance variables

```
q _uplinkStreamToken;
q _downlinkStreamToken;
@"NSDictionary" _streamTokensByParticipantID;
q _combinedAudioStreamToken;
```

## Properties

```
@property (Tq,N,V_uplinkStreamToken) uplinkStreamToken;
@property (Tq,N,V_downlinkStreamToken) downlinkStreamToken;
@property (T@"NSDictionary",&,N,V_streamTokensByParticipantID) streamTokensByParticipantID;
@property (Tq,N,V_combinedAudioStreamToken) combinedAudioStreamToken;
```

## Class methods

```
+[TUMediaTokens supportsSecureCoding];
```

## Instance methods

```
-[TUMediaTokens setDownlinkStreamToken:];
-[TUMediaTokens uplinkStreamToken];
-[TUMediaTokens setCombinedAudioStreamToken:];
-[TUMediaTokens setStreamTokensByParticipantID:];
-[TUMediaTokens combinedAudioStreamToken];
-[TUMediaTokens encodeWithCoder:];
-[TUMediaTokens description];
-[TUMediaTokens initWithCoder:];
-[TUMediaTokens setUplinkStreamToken:];
-[TUMediaTokens downlinkStreamToken];
-[TUMediaTokens streamTokensByParticipantID];
-[TUMediaTokens isEqualToMediaTokens:];
-[TUMediaTokens copyWithZone:];
-[TUMediaTokens isEqual:];
```
