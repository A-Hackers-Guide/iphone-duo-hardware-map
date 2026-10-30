# `TUConversationParticipantCapabilities`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 19 instance variables, 19 properties, 45 instance methods, 1 class methods

## Instance variables

```
B _momentsAvailable;
B _screenSharingAvailable;
B _gondolaCallingAvailable;
B _personaAvailable;
B _gftDowngradeToOneToOneAvailable;
B _uPlusNDowngradeAvailable;
B _uPlusOneScreenShareAvailable;
B _uPlusOneAVLessAvailable;
B _supportsLeaveContext;
B _supportsRequestToScreenShare;
B _uPlusOneVisionToVisionAvailable;
B _photosSharePlayAvailable;
B _translationAvailable;
B _dualCaptureAvailable;
B _groupDualCaptureAvailable;
Q _sharePlayProtocolVersion;
Q _visionFeatureVersion;
Q _visionCallEstablishmentVersion;
Q _nearbyFeatureVersion;
```

## Properties

```
@property (TB,N,GisMomentsAvailable,V_momentsAvailable) momentsAvailable;
@property (TB,N,GisScreenSharingAvailable,V_screenSharingAvailable) screenSharingAvailable;
@property (TB,N,GisGondolaCallingAvailable,V_gondolaCallingAvailable) gondolaCallingAvailable;
@property (TB,N,GisPersonaAvailable,V_personaAvailable) personaAvailable;
@property (TB,N,GisGFTDowngradeToOneToOneAvailable,V_gftDowngradeToOneToOneAvailable) gftDowngradeToOneToOneAvailable;
@property (TB,N,GisUPlusNDowngradeAvailable,V_uPlusNDowngradeAvailable) uPlusNDowngradeAvailable;
@property (TB,N,GisUPlusOneScreenShareAvailable,V_uPlusOneScreenShareAvailable) uPlusOneScreenShareAvailable;
@property (TB,N,GisUPlusOneAVLessAvailable,V_uPlusOneAVLessAvailable) uPlusOneAVLessAvailable;
@property (TB,N,V_supportsLeaveContext) supportsLeaveContext;
@property (TB,N,V_supportsRequestToScreenShare) supportsRequestToScreenShare;
@property (TQ,N,V_sharePlayProtocolVersion) sharePlayProtocolVersion;
@property (TQ,N,V_visionFeatureVersion) visionFeatureVersion;
@property (TQ,N,V_visionCallEstablishmentVersion) visionCallEstablishmentVersion;
@property (TB,N,GisUPlusOneVisionToVisionAvailable,V_uPlusOneVisionToVisionAvailable) uPlusOneVisionToVisionAvailable;
@property (TB,N,GisPhotosSharePlayAvailable,V_photosSharePlayAvailable) photosSharePlayAvailable;
@property (TB,N,GisTranslationAvailable,V_translationAvailable) translationAvailable;
@property (TQ,N,V_nearbyFeatureVersion) nearbyFeatureVersion;
@property (TB,N,GisDualCaptureAvailable,V_dualCaptureAvailable) dualCaptureAvailable;
@property (TB,N,GisGroupDualCaptureAvailable,V_groupDualCaptureAvailable) groupDualCaptureAvailable;
```

## Class methods

```
+[TUConversationParticipantCapabilities supportsSecureCoding];
```

## Instance methods

```
-[TUConversationParticipantCapabilities isMomentsAvailable];
-[TUConversationParticipantCapabilities supportsRequestToScreenShare];
-[TUConversationParticipantCapabilities setUPlusOneScreenShareAvailable:];
-[TUConversationParticipantCapabilities setPersonaAvailable:];
-[TUConversationParticipantCapabilities setMomentsAvailable:];
-[TUConversationParticipantCapabilities setGondolaCallingAvailable:];
-[TUConversationParticipantCapabilities visionCallEstablishmentVersion];
-[TUConversationParticipantCapabilities isGFTDowngradeToOneToOneAvailable];
-[TUConversationParticipantCapabilities isUPlusOneScreenShareAvailable];
-[TUConversationParticipantCapabilities setSharePlayProtocolVersion:];
-[TUConversationParticipantCapabilities isScreenSharingAvailable];
-[TUConversationParticipantCapabilities setNearbyFeatureVersion:];
-[TUConversationParticipantCapabilities setUPlusNDowngradeAvailable:];
-[TUConversationParticipantCapabilities isDualCaptureAvailable];
-[TUConversationParticipantCapabilities isGondolaCallingAvailable];
-[TUConversationParticipantCapabilities setVisionFeatureVersion:];
-[TUConversationParticipantCapabilities setTranslationAvailable:];
-[TUConversationParticipantCapabilities setSupportsRequestToScreenShare:];
-[TUConversationParticipantCapabilities setPhotosSharePlayAvailable:];
-[TUConversationParticipantCapabilities setSupportsLeaveContext:];
-[TUConversationParticipantCapabilities isUPlusNDowngradeAvailable];
-[TUConversationParticipantCapabilities setScreenSharingAvailable:];
-[TUConversationParticipantCapabilities isPersonaAvailable];
-[TUConversationParticipantCapabilities encodeWithCoder:];
-[TUConversationParticipantCapabilities setVisionCallEstablishmentVersion:];
-[TUConversationParticipantCapabilities sharePlayProtocolVersion];
-[TUConversationParticipantCapabilities isEqualToCapabilities:];
-[TUConversationParticipantCapabilities hash];
-[TUConversationParticipantCapabilities isPhotosSharePlayAvailable];
-[TUConversationParticipantCapabilities setGroupDualCaptureAvailable:];
-[TUConversationParticipantCapabilities description];
-[TUConversationParticipantCapabilities initWithCoder:];
-[TUConversationParticipantCapabilities setDualCaptureAvailable:];
-[TUConversationParticipantCapabilities copyWithZone:];
-[TUConversationParticipantCapabilities nearbyFeatureVersion];
-[TUConversationParticipantCapabilities isUPlusOneVisionToVisionAvailable];
-[TUConversationParticipantCapabilities isEqual:];
-[TUConversationParticipantCapabilities supportsLeaveContext];
-[TUConversationParticipantCapabilities isUPlusOneAVLessAvailable];
-[TUConversationParticipantCapabilities isGroupDualCaptureAvailable];
-[TUConversationParticipantCapabilities isTranslationAvailable];
-[TUConversationParticipantCapabilities setGftDowngradeToOneToOneAvailable:];
-[TUConversationParticipantCapabilities setUPlusOneAVLessAvailable:];
-[TUConversationParticipantCapabilities visionFeatureVersion];
-[TUConversationParticipantCapabilities setUPlusOneVisionToVisionAvailable:];
```
