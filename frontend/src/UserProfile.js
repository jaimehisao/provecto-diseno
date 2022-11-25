var UserProfile = (function () {
	var user_name = "";

	var getName = function () {
		return user_name;
	};

	var setName = function (name) {
		user_name = name;
	};

	return {
		getName: getName,
		setName: setName,
	};
})();

export default UserProfile;
