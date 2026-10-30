# `TUConversationActivityMetadata`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUSanitizedCopying`, `NSSecureCoding`
- 13 instance variables, 19 properties, 39 instance methods, 2 class methods

## Instance variables

```
B _supportsContinuationOnTV;
B _supportsActivityPreviews;
@"TUConversationActivityContext" _context;
@"NSData" _linkMetadatablob;
@"NSURL" _fallbackURL;
@"NSURL" _invitationURL;
@"NSString" _title;
@"NSString" _subTitle;
@"NSData" _imageData;
q _preferredBroadcastingAttributes;
@"TUConversationActivitySceneAssociationBehavior" _sceneAssociationBehavior;
q _lifetimePolicy;
@"TUSandboxExtendedURL" _imageFileURL;
```

## Properties

```
@property (T@"TUSandboxExtendedURL",&,N,V_imageFileURL) imageFileURL;
@property (T@"TUConversationActivityContext",R,C,N,V_context) context;
@property (T@"NSData",C,N,V_linkMetadatablob) linkMetadatablob;
@property (T@"NSURL",R,C,N,V_fallbackURL) fallbackURL;
@property (T@"NSURL",R,C,N,V_invitationURL) invitationURL;
@property (TB,N,V_supportsContinuationOnTV) supportsContinuationOnTV;
@property (T@"NSString",R,C,N,V_title) title;
@property (T@"NSString",R,C,N,V_subTitle) subTitle;
@property (T@"NSData",C,N,V_imageData) imageData;
@property (Tq,N,V_preferredBroadcastingAttributes) preferredBroadcastingAttributes;
@property (T@"TUConversationActivitySceneAssociationBehavior",R,C,N,V_sceneAssociationBehavior) sceneAssociationBehavior;
@property (TB,R,N,V_supportsActivityPreviews) supportsActivityPreviews;
@property (Tq,R,N) contentAssociation;
@property (Tq,R,N,V_lifetimePolicy) lifetimePolicy;
@property (TQ,R) length;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUConversationActivityMetadata supportsSecureCoding];
+[TUConversationActivityMetadata activityMetadataWithDataBlob:];
```

## Instance methods

```
-[TUConversationActivityMetadata serializedData];
-[TUConversationActivityMetadata setImageData:];
-[TUConversationActivityMetadata imageData];
-[TUConversationActivityMetadata fallbackURL];
-[TUConversationActivityMetadata length];
-[TUConversationActivityMetadata title];
-[TUConversationActivityMetadata encodeWithCoder:];
-[TUConversationActivityMetadata sanitizedCopy];
-[TUConversationActivityMetadata hash];
-[TUConversationActivityMetadata description];
-[TUConversationActivityMetadata initWithCoder:];
-[TUConversationActivityMetadata sanitizedCopyWithZone:];
-[TUConversationActivityMetadata copyWithZone:];
-[TUConversationActivityMetadata context];
-[TUConversationActivityMetadata isEqual:];
-[TUConversationActivityMetadata imageFileURL];
-[TUConversationActivityMetadata subTitle];
-[TUConversationActivityMetadata invitationURL];
-[TUConversationActivityMetadata setImageFileURL:];
-[TUConversationActivityMetadata isEquivalentToActivityMetadata:];
-[TUConversationActivityMetadata preferredBroadcastingAttributes];
-[TUConversationActivityMetadata saveImageToDisk];
-[TUConversationActivityMetadata _createImageFolderIfNeeded];
-[TUConversationActivityMetadata _filePathForImage];
-[TUConversationActivityMetadata _imagePreviewDirectoryPath];
-[TUConversationActivityMetadata _isEqualToActivityMetadata:];
-[TUConversationActivityMetadata contentAssociation];
-[TUConversationActivityMetadata initWithContext:linkMetadata:fallbackURL:invitationURL:supportsContinuationOnTV:title:subTitle:imageData:];
-[TUConversationActivityMetadata initWithContext:linkMetadata:fallbackURL:invitationURL:supportsContinuationOnTV:title:subTitle:imageData:preferredBroadcastingAttributes:sceneAssociationBehavior:supportsActivityPreviews:];
-[TUConversationActivityMetadata initWithContext:linkMetadata:fallbackURL:invitationURL:supportsContinuationOnTV:title:subTitle:imageData:preferredBroadcastingAttributes:sceneAssociationBehavior:supportsActivityPreviews:lifetimePolicy:];
-[TUConversationActivityMetadata lifetimePolicy];
-[TUConversationActivityMetadata linkMetadatablob];
-[TUConversationActivityMetadata removeImageDiskFile];
-[TUConversationActivityMetadata sceneAssociationBehavior];
-[TUConversationActivityMetadata setLinkMetadatablob:];
-[TUConversationActivityMetadata setPreferredBroadcastingAttributes:];
-[TUConversationActivityMetadata setSupportsContinuationOnTV:];
-[TUConversationActivityMetadata supportsActivityPreviews];
-[TUConversationActivityMetadata supportsContinuationOnTV];
```
