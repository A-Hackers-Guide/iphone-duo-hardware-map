# `BLSHTapToRadarDescriptor`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _userInitiated;
Q _designation;
@"NSString" _radarTitle;
@"NSString" _radarDescription;
@"NSString" _bundleID;
@"NSArray" _keywordIDs;
@"NSArray" _attachments;
q _componentID;
@"NSString" _componentName;
@"NSString" _componentVersion;
@"NSString" _ttrPromptHeader;
@"NSString" _ttrPromptMessage;
@"NSString" _ttrDisplayReason;
@"NSDate" _timeOfIssue;
```

## Properties

```
@property (TQ,R,N,V_designation) designation;
@property (T@"NSString",R,N,V_radarTitle) radarTitle;
@property (T@"NSString",R,N,V_radarDescription) radarDescription;
@property (T@"NSString",C,N,V_bundleID) bundleID;
@property (T@"NSArray",C,N,V_keywordIDs) keywordIDs;
@property (T@"NSArray",C,N,V_attachments) attachments;
@property (Tq,N,V_componentID) componentID;
@property (T@"NSString",C,N,V_componentName) componentName;
@property (T@"NSString",C,N,V_componentVersion) componentVersion;
@property (T@"NSString",C,N,V_ttrPromptHeader) ttrPromptHeader;
@property (T@"NSString",C,N,V_ttrPromptMessage) ttrPromptMessage;
@property (T@"NSString",C,N,V_ttrDisplayReason) ttrDisplayReason;
@property (T@"NSDate",C,N,V_timeOfIssue) timeOfIssue;
@property (TB,N,V_userInitiated) userInitiated;
```

## Instance methods

```
-[BLSHTapToRadarDescriptor setAttachments:];
-[BLSHTapToRadarDescriptor userInitiated];
-[BLSHTapToRadarDescriptor setBundleID:];
-[BLSHTapToRadarDescriptor attachments];
-[BLSHTapToRadarDescriptor componentName];
-[BLSHTapToRadarDescriptor setUserInitiated:];
-[BLSHTapToRadarDescriptor bundleID];
-[BLSHTapToRadarDescriptor setComponentID:];
-[BLSHTapToRadarDescriptor componentID];
-[BLSHTapToRadarDescriptor componentVersion];
-[BLSHTapToRadarDescriptor radarDescription];
-[BLSHTapToRadarDescriptor setComponentName:];
-[BLSHTapToRadarDescriptor setComponentVersion:];
-[BLSHTapToRadarDescriptor setTimeOfIssue:];
-[BLSHTapToRadarDescriptor designation];
-[BLSHTapToRadarDescriptor radarTitle];
-[BLSHTapToRadarDescriptor setKeywordIDs:];
-[BLSHTapToRadarDescriptor keywordIDs];
-[BLSHTapToRadarDescriptor ttrPromptHeader];
-[BLSHTapToRadarDescriptor initWithDesignation:radarTitle:radarDescription:];
-[BLSHTapToRadarDescriptor setTtrDisplayReason:];
-[BLSHTapToRadarDescriptor setTtrPromptHeader:];
-[BLSHTapToRadarDescriptor setTtrPromptMessage:];
-[BLSHTapToRadarDescriptor timeOfIssue];
-[BLSHTapToRadarDescriptor ttrDisplayReason];
-[BLSHTapToRadarDescriptor ttrPromptMessage];
```
