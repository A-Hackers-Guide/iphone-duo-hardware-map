# `TUScreenSharingRequest`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 8 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _shouldSendLegacyInvite;
@"TUHandle" _handle;
Q _participantIdentifier;
q _type;
q _originType;
@"NSUUID" _UUID;
@"TUScreenSharingRequestMetadata" _metadata;
```

## Properties

```
@property (T@"NSUUID",C,N,V_UUID) UUID;
@property (T@"TUHandle",R,N,V_handle) handle;
@property (TQ,R,N,V_participantIdentifier) participantIdentifier;
@property (Tq,R,N,V_type) type;
@property (TB,R,N) isLocallyOriginated;
@property (Tq,R,N,V_originType) originType;
@property (TB,R,N,V_shouldSendLegacyInvite) shouldSendLegacyInvite;
@property (T@"TUScreenSharingRequestMetadata",R,C,N,V_metadata) metadata;
```

## Class methods

```
+[TUScreenSharingRequest supportsSecureCoding];
```

## Instance methods

```
-[TUScreenSharingRequest setUUID:];
-[TUScreenSharingRequest UUID];
-[TUScreenSharingRequest participantIdentifier];
-[TUScreenSharingRequest metadata];
-[TUScreenSharingRequest handle];
-[TUScreenSharingRequest type];
-[TUScreenSharingRequest encodeWithCoder:];
-[TUScreenSharingRequest hash];
-[TUScreenSharingRequest description];
-[TUScreenSharingRequest initWithCoder:];
-[TUScreenSharingRequest isEqualToRequest:];
-[TUScreenSharingRequest copyWithZone:];
-[TUScreenSharingRequest isEqual:];
-[TUScreenSharingRequest initWithHandle:shareMyScreen:originType:shouldSendLegacyInvite:metadata:];
-[TUScreenSharingRequest initWithHandle:type:originType:UUID:participantIdentifier:metadata:];
-[TUScreenSharingRequest initWithHandle:type:originType:UUID:participantIdentifier:shouldSendLegacyInvite:metadata:];
-[TUScreenSharingRequest isLocallyOriginated];
-[TUScreenSharingRequest originType];
-[TUScreenSharingRequest shouldSendLegacyInvite];
```
