class AmazingFeature:
    def __init__(self, feature_name):
        self.feature_name = feature_name

    def show_feature(self):
        print("This is an amazing feature: {}".format(self.feature_name))

feature = AmazingFeature("Awesome functionality")
feature.show_feature()