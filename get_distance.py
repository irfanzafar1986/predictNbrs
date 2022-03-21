src_info_added=nbrs.merge(nw,how='inner',left_on=['sourcesite','sourcecell'],right_on=['site','cell'])
tgt_info_added=src_info_added.merge(nw,how='inner',left_on=['targetsite','targetcell'],right_on=['site','cell'])
tgt_info_added['distance']= tgt_info_added.apply(lambda row:
                                           geo.haversine_distance(row['latitude_x'],row['longitude_x'],row['latitude_y'],row['longitude_y']),axis=1)
