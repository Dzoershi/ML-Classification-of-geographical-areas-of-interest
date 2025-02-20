#compute change of the state of the area variables categorical variables -> binary ones
test_df['area_change_0_1'] = (test_df['change_status_date0'] != test_df['change_status_date1']).apply(lambda x: 1 if x else 0)

test_df['area_change_1_2'] = (test_df['change_status_date1'] != test_df['change_status_date2']).apply(lambda x: 1 if x else 0)

test_df['area_change_2_3'] = (test_df['change_status_date2'] != test_df['change_status_date3']).apply(lambda x: 1 if x else 0)

test_df['area_change_3_4'] = (test_df['change_status_date3'] != test_df['change_status_date4']).apply(lambda x: 1 if x else 0)

# compute a weighted average of the RGB means and stds over the 5 dates
test_df['red_channel_mean'] = ( test_df['img_red_mean_date1'] + 2*test_df['img_red_mean_date2'] + 3*test_df['img_red_mean_date3'] + 4*test_df['img_red_mean_date4'] + 5*test_df['img_red_mean_date5']) / 5

test_df['blue_channel_mean'] = ( test_df['img_blue_mean_date1'] + 2*test_df['img_blue_mean_date2'] + 3*test_df['img_blue_mean_date3'] + 4*test_df['img_blue_mean_date4'] + 5*test_df['img_blue_mean_date5']) / 5

test_df['green_channel_mean'] = ( test_df['img_green_mean_date1'] + 2*test_df['img_green_mean_date2'] + 3*test_df['img_green_mean_date3'] + 4*test_df['img_green_mean_date4'] + 5*test_df['img_green_mean_date5']) / 5

test_df['red_channel_std'] = ( test_df['img_red_std_date1'] + 2*test_df['img_red_std_date2'] + 3*test_df['img_red_std_date3'] + 4*test_df['img_red_std_date4'] + 5*test_df['img_red_std_date5']) / 5

test_df['blue_channel_std'] = ( test_df['img_blue_std_date1'] + 2*test_df['img_blue_std_date2'] + 3*test_df['img_blue_std_date3'] + 4*test_df['img_blue_std_date4'] + 5*test_df['img_blue_std_date5']) / 5

test_df['green_channel_std'] = ( test_df['img_green_std_date1'] + 2*test_df['img_green_std_date2'] + 3*test_df['img_green_std_date3'] + 4*test_df['img_green_std_date4'] + 5*test_df['img_green_std_date5']) / 5