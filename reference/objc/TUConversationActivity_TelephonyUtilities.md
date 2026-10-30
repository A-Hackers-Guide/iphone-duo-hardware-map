# `TUConversationActivity`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 16 instance variables, 21 properties, 62 instance methods, 3 class methods

## Instance variables

```
B _supported;
B _requiresParticipantTranslation;
B _systemActivity;
B _startWhenStaged;
@"NSUUID" _UUID;
@"NSData" _applicationContext;
@"NSString" _bundleIdentifier;
@"NSString" _activityIdentifier;
@"TUConversationActivityMetadata" _metadata;
@"TUHandle" _originator;
@"TUHandle" _trustedFromHandle;
@"NSDate" _timestamp;
@"NSString" _fallbackApplicationName;
@"NSString" _staticIdentifier;
@"NSString" _activationSceneIdentifier;
@"TUScreenShareAttributes" _screenShareAttributes;
```

## Properties

```
@property (T@"NSString",C,N,V_activityIdentifier) activityIdentifier;
@property (T@"NSUUID",&,N,V_UUID) UUID;
@property (T@"TUConversationActivityMetadata",&,N,V_metadata) metadata;
@property (T@"NSData",C,N,V_applicationContext) applicationContext;
@property (T@"NSString",C,N,V_bundleIdentifier) bundleIdentifier;
@property (TB,N,GisSupported,V_supported) supported;
@property (T@"TUHandle",C,N,V_originator) originator;
@property (T@"TUHandle",C,N,V_trustedFromHandle) trustedFromHandle;
@property (T@"NSDate",C,N,V_timestamp) timestamp;
@property (T@"NSString",C,N,V_fallbackApplicationName) fallbackApplicationName;
@property (TB,N,GisSystemActivity,V_systemActivity) systemActivity;
@property (T@"NSString",C,N,V_staticIdentifier) staticIdentifier;
@property (TB,N,V_startWhenStaged) startWhenStaged;
@property (TB,N,V_requiresParticipantTranslation) requiresParticipantTranslation;
@property (T@"NSString",C,N,V_activationSceneIdentifier) activationSceneIdentifier;
@property (T@"TUScreenShareAttributes",C,N,V_screenShareAttributes) screenShareAttributes;
@property (T@"NSString",R,C,N) representativeBundleIdentifier;
@property (T@"TUConversationActivityContext",R,C,N) activityContext;
@property (TB,R,N,GisEligibleForHandoff) eligibleForHandoff;
@property (TB,R,N,GisEligibleForWebBrowser) eligibleForWebBrowser;
@property (TB,R,N,GisPlaceholderActivity) placeholderActivity;
```

## Class methods

```
+[TUConversationActivity supportsSecureCoding];
+[TUConversationActivity lookupApplicationNameForBundleIdentifier:];
+[TUConversationActivity placeholderActivity];
```

## Instance methods

```
-[TUConversationActivity activityIdentifier];
-[TUConversationActivity setSupported:];
-[TUConversationActivity setApplicationContext:];
-[TUConversationActivity setTimestamp:];
-[TUConversationActivity setUUID:];
-[TUConversationActivity setActivityIdentifier:];
-[TUConversationActivity isSupported];
-[TUConversationActivity UUID];
-[TUConversationActivity timestamp];
-[TUConversationActivity bundleIdentifier];
-[TUConversationActivity setOriginator:];
-[TUConversationActivity metadata];
-[TUConversationActivity applicationContext];
-[TUConversationActivity encodeWithCoder:];
-[TUConversationActivity setMetadata:];
-[TUConversationActivity sanitizedCopy];
-[TUConversationActivity hash];
-[TUConversationActivity setScreenShareAttributes:];
-[TUConversationActivity description];
-[TUConversationActivity initWithCoder:];
-[TUConversationActivity sanitizedCopyWithZone:];
-[TUConversationActivity localizedApplicationName];
-[TUConversationActivity setBundleIdentifier:];
-[TUConversationActivity copyWithZone:];
-[TUConversationActivity isEqual:];
-[TUConversationActivity originator];
-[TUConversationActivity screenShareAttributes];
-[TUConversationActivity isEligibleForHandoff];
-[TUConversationActivity concatenatedMetadataDescription];
-[TUConversationActivity fallbackApplicationName];
-[TUConversationActivity activityContext];
-[TUConversationActivity startWhenStaged];
-[TUConversationActivity activationSceneIdentifier];
-[TUConversationActivity concatenatedDescription];
-[TUConversationActivity initWithBundleIdentifier:metadata:applicationContext:uuid:activityIdentifier:];
-[TUConversationActivity initWithBundleIdentifier:metadata:applicationContext:uuid:activityIdentifier:fallbackApplicationName:];
-[TUConversationActivity initWithCreationRequest:bundleIdentifier:systemActivity:];
-[TUConversationActivity initWithCreationRequest:bundleIdentifier:systemActivity:requiresParticipantTranslation:];
-[TUConversationActivity initWithMetadata:applicationContext:uuid:activityIdentifier:];
-[TUConversationActivity isAccessibilityCaptions];
-[TUConversationActivity isEligibleForWebBrowser];
-[TUConversationActivity isEqualToConversationActivity:];
-[TUConversationActivity isEquivalentToActivity:];
-[TUConversationActivity isPlaceholderActivity];
-[TUConversationActivity isScreenSharingActivity];
-[TUConversationActivity isStaticActivity];
-[TUConversationActivity isSystemActivity];
-[TUConversationActivity isTranslationActivity];
-[TUConversationActivity platformScreenSharingBundleIdentifier];
-[TUConversationActivity representativeBundleIdentifier];
-[TUConversationActivity representativeDisplayName];
-[TUConversationActivity requiresParticipantTranslation];
-[TUConversationActivity setActivationSceneIdentifier:];
-[TUConversationActivity setActivityContext:];
-[TUConversationActivity setFallbackApplicationName:];
-[TUConversationActivity setRequiresParticipantTranslation:];
-[TUConversationActivity setStartWhenStaged:];
-[TUConversationActivity setStaticIdentifier:];
-[TUConversationActivity setSystemActivity:];
-[TUConversationActivity setTrustedFromHandle:];
-[TUConversationActivity staticIdentifier];
-[TUConversationActivity trustedFromHandle];
```
