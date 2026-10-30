# `UIWebClip`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 42 instance variables, 39 properties, 116 instance methods, 24 class methods

## Instance variables

```
@"NSString" identifier;
@"NSURL" pageURL;
@"NSArray" icons;
Q currentIconIndex;
@"NSURL" startupImageURL;
@"NSURL" startupLandscapeImageURL;
@"NSString" title;
@"NSString" applicationBundleIdentifier;
@"NSString" placeholderBundleIdentifier;
@"NSURL" manifestId;
Q bundleVersion;
B fullScreen;
B classicMode;
B removalDisallowed;
B iconIsScreenShotBased;
B iconIsPrecomposed;
B iconIsPrerendered;
Q supportedOrientations;
q statusBarStyle;
@"UIImage" iconImage;
@"UIImage" startupImage;
@"UIImage" startupLandscapeImage;
@"UIImage" initialLaunchImage;
@"<WebClipDelegate>" delegate;
@"NSMutableData" _customIconData;
@"NSURLConnection" _iconConnection;
@"NSMutableData" _customStartupImageData;
@"NSURLConnection" _startupImageConnection;
@"NSMutableData" _customStartupLandscapeImageData;
@"NSURLConnection" _startupLandscapeImageConnection;
@"NSDictionary" _readOnlyDictionaryRepresentation;
B _isAppClip;
B _scenelessBackgroundLaunch;
B _ignoreManifestScope;
B _configurationIsManaged;
@"NSSet" _trustedClientBundleIdentifiers;
@"UIImage" darkIconImage;
@"UIImage" tintableIconImage;
@"NSString" _shortcutIdentifier;
Q _contentMode;
Q _webClipStatusBarStyle;
Q _eligibilityStatus;
```

## Properties

```
@property (T@"NSString",C,Videntifier) identifier;
@property (T@"NSUUID",R,N) uuid;
@property (T@"NSURL",&,N,VpageURL) pageURL;
@property (T@"NSArray",&,Vicons) icons;
@property (T@"NSURL",&,VstartupImageURL) startupImageURL;
@property (T@"NSURL",&,VstartupLandscapeImageURL) startupLandscapeImageURL;
@property (T@"NSString",C,N,Vtitle) title;
@property (T@"NSString",C,N,VapplicationBundleIdentifier) applicationBundleIdentifier;
@property (T@"NSString",C,N,VplaceholderBundleIdentifier) placeholderBundleIdentifier;
@property (T@"NSSet",R,N,V_trustedClientBundleIdentifiers) trustedClientBundleIdentifiers;
@property (T@"NSURL",C,N,VmanifestId) manifestId;
@property (T@"NSString",C,N,V_shortcutIdentifier) shortcutIdentifier;
@property (T@"NSURL",R,N) applicationLaunchURL;
@property (T@"NSUserActivity",R,N) appClipUserActivity;
@property (TQ,R,N,VbundleVersion) bundleVersion;
@property (TB) fullScreen;
@property (TB,R) alternativeFullScreen;
@property (TB,VclassicMode) classicMode;
@property (TB,VremovalDisallowed) removalDisallowed;
@property (TB,V_isAppClip) isAppClip;
@property (TB,V_scenelessBackgroundLaunch) scenelessBackgroundLaunch;
@property (TQ,V_contentMode) contentMode;
@property (TB,V_ignoreManifestScope) ignoreManifestScope;
@property (TB,V_configurationIsManaged) configurationIsManaged;
@property (TB,R,ViconIsScreenShotBased) iconIsScreenShotBased;
@property (TB,R,ViconIsPrecomposed) iconIsPrecomposed;
@property (TB,R,ViconIsPrerendered) iconIsPrerendered;
@property (TQ,VsupportedOrientations) supportedOrientations;
@property (Tq,VstatusBarStyle) statusBarStyle;
@property (TQ,N,V_webClipStatusBarStyle) webClipStatusBarStyle;
@property (T@"NSString",R) iconImagePath;
@property (T@"UIImage",R,&,N) iconImage;
@property (T@"UIImage",&,N,VdarkIconImage) darkIconImage;
@property (T@"UIImage",&,N,VtintableIconImage) tintableIconImage;
@property (T@"UIImage",&,N,VstartupImage) startupImage;
@property (T@"UIImage",&,N,VstartupLandscapeImage) startupLandscapeImage;
@property (T@"UIImage",&,N,VinitialLaunchImage) initialLaunchImage;
@property (T@"<WebClipDelegate>",W,N,Vdelegate) delegate;
@property (TQ,R,V_eligibilityStatus) eligibilityStatus;
```

## Class methods

```
+[UIWebClip webClipWithURL:];
+[UIWebClip _contentForMetaName:inWebDocumentView:];
+[UIWebClip _determineEligibility];
+[UIWebClip _normalizedWebClipIdentifierFromBundleIdentifier:];
+[UIWebClip _webClipFullScreenValueForMetaTagContent:];
+[UIWebClip _webClipOrientationsForMetaTagContent:];
+[UIWebClip _webClipStatusBarStyleForMetaTagContent:];
+[UIWebClip appClips];
+[UIWebClip bundleIdentifierContainsWebClipIdentifier:];
+[UIWebClip clipsIncludingWebClips:includingAppClips:];
+[UIWebClip clipsIncludingWebClips:includingAppClips:trustedByClientBundleIdentifier:];
+[UIWebClip pathForWebClipCacheWithIdentifier:];
+[UIWebClip pathForWebClipStorageWithIdentifier:];
+[UIWebClip pathForWebClipWithIdentifier:];
+[UIWebClip urlForWebClipWithIdentifier:];
+[UIWebClip webClipIconsForWebClipLinkTags:pageURL:];
+[UIWebClip webClipIdentifierFromBundleIdentifier:];
+[UIWebClip webClipStatusBarStyleForWebDocumentView:];
+[UIWebClip webClipWithDictionaryRepresentation:];
+[UIWebClip webClipWithIdentifier:];
+[UIWebClip webClipWithIdentifierExists:];
+[UIWebClip webClipWithUUID:];
+[UIWebClip webClips];
+[UIWebClip webClipsDirectoryPath];
```

## Instance methods

```
-[UIWebClip bundleVersion];
-[UIWebClip pageURL];
-[UIWebClip contentMode];
-[UIWebClip setContentMode:];
-[UIWebClip uuid];
-[UIWebClip identifier];
-[UIWebClip _reloadProperties];
-[UIWebClip dealloc];
-[UIWebClip setIsAppClip:];
-[UIWebClip bundleIdentifier];
-[UIWebClip icons];
-[UIWebClip _info];
-[UIWebClip setFullScreen:];
-[UIWebClip setClassicMode:];
-[UIWebClip setApplicationBundleIdentifier:];
-[UIWebClip setIdentifier:];
-[UIWebClip setDelegate:];
-[UIWebClip title];
-[UIWebClip iconImage];
-[UIWebClip applicationBundleIdentifier];
-[UIWebClip delegate];
-[UIWebClip connection:didFailWithError:];
-[UIWebClip setTitle:];
-[UIWebClip setIcons:];
-[UIWebClip statusBarStyle];
-[UIWebClip setStatusBarStyle:];
-[UIWebClip classicMode];
-[UIWebClip setPageURL:];
-[UIWebClip isAppClip];
-[UIWebClip _writeImage:toDiskWithFileName:];
-[UIWebClip configureWithMetaTags:linkTags:];
-[UIWebClip setPlaceholderBundleIdentifier:];
-[UIWebClip startupImageURL];
-[UIWebClip _bundleImageWithName:];
-[UIWebClip _bundleResourceWithName:];
-[UIWebClip _createApplicationRecord];
-[UIWebClip _createPlaceholderBundleIdentifier];
-[UIWebClip _defaultBrowserName];
-[UIWebClip _hasPlaceholderBundle];
-[UIWebClip _initWithIdentifier:dictionaryRepresentation:];
-[UIWebClip _launchURLWithScheme:];
-[UIWebClip _readPropertiesFromInfoPlist:];
-[UIWebClip _removePlaceholderBundleAndClearBadge];
-[UIWebClip _removePlaceholderBundleWithCompletion:];
-[UIWebClip _requiresPlaceholderBundle];
-[UIWebClip _setIconImage:isPrecomposed:isScreenShotBased:];
-[UIWebClip _subjectToEligibilityUpdates];
-[UIWebClip _updateWebClipWithEligibility:];
-[UIWebClip _writeIconImage:toDiskWithFileName:];
-[UIWebClip addTrustedClientBundleIdentifier:];
-[UIWebClip alternativeFullScreen];
-[UIWebClip appClipUserActivity];
-[UIWebClip applicationLaunchURL];
-[UIWebClip cancelMediaUpdate];
-[UIWebClip configurationIsManaged];
-[UIWebClip connection:didReceiveData:];
-[UIWebClip connection:didReceiveResponse:];
-[UIWebClip connectionDidFinishLoading:];
-[UIWebClip coordinator:canceledWithReason:client:];
-[UIWebClip coordinatorDidCompleteSuccessfully:forApplicationRecord:];
-[UIWebClip createOnDisk];
-[UIWebClip darkIconImage];
-[UIWebClip eligibilityAlert:];
-[UIWebClip eligibilityStatus];
-[UIWebClip ensurePlaceholderBundle];
-[UIWebClip fullScreen];
-[UIWebClip generateIconImageForFormat:scale:];
-[UIWebClip getStartupImage:];
-[UIWebClip iconImagePath];
-[UIWebClip iconIsPrecomposed];
-[UIWebClip iconIsPrerendered];
-[UIWebClip iconIsScreenShotBased];
-[UIWebClip ignoreManifestScope];
-[UIWebClip initialLaunchImage];
-[UIWebClip manifestId];
-[UIWebClip needsWebAppDeletionStrings];
-[UIWebClip placeholderBundleIdentifier];
-[UIWebClip removalDisallowed];
-[UIWebClip removeFromDisk];
-[UIWebClip requestCustomIconUpdate];
-[UIWebClip requestCustomLandscapeStartupImageUpdate];
-[UIWebClip requestCustomPortraitStartupImageUpdate];
-[UIWebClip requestIconUpdateInSpringBoard];
-[UIWebClip scenelessBackgroundLaunch];
-[UIWebClip setConfigurationIsManaged:];
-[UIWebClip setContentModeWithString:];
-[UIWebClip setDarkIconImage:];
-[UIWebClip setIconImage:isPrecomposed:];
-[UIWebClip setIconImageFromScreenshot:];
-[UIWebClip setIgnoreManifestScope:];
-[UIWebClip setInitialLaunchImage:];
-[UIWebClip setManifestId:];
-[UIWebClip setRemovalDisallowed:];
-[UIWebClip setScenelessBackgroundLaunch:];
-[UIWebClip setShortcutIdentifier:];
-[UIWebClip setStartupImage:];
-[UIWebClip setStartupImageURL:];
-[UIWebClip setStartupLandscapeImage:];
-[UIWebClip setStartupLandscapeImageURL:];
-[UIWebClip setSupportedOrientations:];
-[UIWebClip setTintableIconImage:];
-[UIWebClip setWebClipStatusBarStyle:];
-[UIWebClip shortcutIdentifier];
-[UIWebClip startupImage];
-[UIWebClip startupLandscapeImage];
-[UIWebClip startupLandscapeImageURL];
-[UIWebClip stopLoadingCustomIcon];
-[UIWebClip stopLoadingStartupImage];
-[UIWebClip stopLoadingStartupLandscapeImage];
-[UIWebClip supportedOrientations];
-[UIWebClip tintableIconImage];
-[UIWebClip trustedClientBundleIdentifiers];
-[UIWebClip tryLoadingNextCustomIcon];
-[UIWebClip updateCustomMediaLocationsWithWebClipLinkTags:baseURL:];
-[UIWebClip updateOnDisk];
-[UIWebClip webClipStatusBarStyle];
```
